# Use the official Python 3.11 image as the base image
FROM python:3.11

# Install necessary system packages for building Python modules
RUN apt-get update && apt-get install -y python3-distutils build-essential

# Upgrade pip, setuptools, and wheel to the latest versions
RUN pip install --upgrade pip setuptools wheel

# Set the working directory inside the container to /app
WORKDIR /app

# Copy requirements.txt into the container (used for caching dependencies)
COPY requirements.txt .

# Install the dependencies listed in requirements.txt without caching
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files into the container
COPY . .

# Expose port 8080 to allow external access to the application
EXPOSE 8080

# Set the command to run the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
