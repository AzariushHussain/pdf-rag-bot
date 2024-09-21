# Use an official Python 3.12.5 runtime as a base image
FROM python:3.12.5-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Specify the command to run your Streamlit app
CMD ["streamlit", "run", "app.py", "--server.headless", "true"]
