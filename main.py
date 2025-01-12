
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
import uvicorn
import ollama
from prompt import PROMPT

# Create the FastAPI app
app = FastAPI()

# Directories
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

# Set up static and templates directories
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Serve the uploaded images
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

def create_description(image_path):
    response = ollama.chat(
        model="llama3.2-vision",
        messages=[
            {
                "role": "user",
                "content": PROMPT,
                "images": [image_path],
            }
        ],
    )

    description = response["message"]["content"]
    print(description)
    return description

@app.get("/", response_class=HTMLResponse)
async def serve_home(request: Request):
    """
    Serve the main HTML interface for the app.
    """
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/upload", response_class=HTMLResponse)
async def upload_image(request: Request, image: UploadFile = File(...)):
    """
    Handle image upload, save it locally, and return a page with the description.
    """
    try:
        # Save the uploaded image locally
        file_path = f"{UPLOAD_DIR}/{image.filename}"
        with open(file_path, "wb") as f:
            f.write(await image.read())

        # Get image description
        description = create_description(file_path)

        # Render the description
        return JSONResponse(content={"description": description})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


# Run the app with uvicorn
if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8000)
