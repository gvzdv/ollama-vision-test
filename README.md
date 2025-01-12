# Ollama Vision Test

A simple web application for uploading images, generating descriptions using **LLaMa-3.2** via **ollama** Python library on the backend, and displaying them on the frontend. The backend is powered by **FastAPI**, and the frontend uses **HTML**, **CSS**, and **JavaScript**.

## Features
- Drag-and-drop image upload functionality.
- Real-time Markdown rendering of descriptions.
- Backend image processing with FastAPI.
- Dynamic updates using Fetch API.

## Requirements
- Python 3.12
- At least 8GB VRAM

## Setup

```bash
# Clone the repository
git clone https://github.com/gvzdv/ollama-vision-test
cd ollama-vision-test

# Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn main:app --reload
```

## Folder Structure

```
ollama-vision-test/
├── main.py           # FastAPI backend
├── templates/        # Jinja2 templates
│   ├── index.html
├── static/           # Static files
│   ├── styles.css
│   ├── script.js
├── uploads/          # Directory for uploaded images
├── .gitignore        # Ignored files
├── README.md         # Project documentation
```

## Usage

1. Start the FastAPI server:
   ```bash
   python -m uvicorn main:app --reload
   ```

2. Open your browser and navigate to:
http://127.0.0.1:8000

3. Drag and drop an image into the app to see the generated description.

## Known Issues
- Multiple edge cases are not accounted for (non-image file types, file size restriction, file cleaning, etc...)
- Chat history and interface not implemented
- Streaming not implemented
- Insufficient error logging

## License
This project is licensed under the MIT License.