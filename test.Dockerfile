# Use an official Python runtime as a base image
FROM python:3.12-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY src/ /app/src/

# Install any needed packages specified in requirements.txt
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Run tests when the container launches
CMD ["python", "src/test_calculators.py"]