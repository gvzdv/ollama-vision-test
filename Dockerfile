# Use an official Python runtime as a base image
FROM python:3.10-slim

# Set environment variables to prevent Python from buffering logs
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies required for Ollama
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install the Ollama CLI
RUN curl -fsSL https://ollama.com/install.sh | sh

# Ensure Ollama is in the PATH
ENV PATH="/root/.ollama/bin:${PATH}"

# Copy the application code into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Pull the required model before starting the application
RUN ollama serve & sleep 10 && ollama pull llama3.2-vision

# Expose the port the app runs on
EXPOSE 8000

# Start the Ollama service and the FastAPI app
CMD ollama serve & uvicorn main:app --host 0.0.0.0 --port 8000