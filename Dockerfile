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

# Run flask app when the container launches : flask --app hostit run --debug on port 5000
CMD ["flask", "run", "--app", "hostit", "--debug"]
