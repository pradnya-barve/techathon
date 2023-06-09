# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Install required system packages for the app
RUN apt-get update && apt-get install -y \
    freeglut3-dev \
    libgtk2.0-dev \
    gcc \
    tesseract-ocr

# Copy the requirements file into the container and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code into the container
COPY app.py .

# Expose port 8501 for Streamlit to listen on
EXPOSE 8501

# Run the command to start Streamlit when the container starts up
CMD ["streamlit", "run", "app.py", "--server.port", "8501"]
