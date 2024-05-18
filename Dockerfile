# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /hostit

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files to the working directory
COPY . .

# Expose the Flask port
EXPOSE 5000

# Set the Flask app environment variable and run the application
CMD flask --app hostit init-db && flask --app hostit run --host=0.0.0.0 --port=5000 --debug

