# Use official Python image from Docker Hub
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements.txt from local machine to container
COPY requirements.txt .

# Install all Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into container
COPY . .

# Inform Docker that container uses port 5000
EXPOSE 5000

# Command to run Flask application
CMD ["python", "app.py"]