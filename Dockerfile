# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /html2md

# Copy the requirements file into the container at /app
COPY requirements.txt /html2md/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . /html2md/

# Expose the ports used by your application
EXPOSE 5000 8080

# Set environment variables if necessary (optional)
# ENV VARIABLE_NAME=value

# Command to run the API server (adjust as per your project structure)
CMD ["uvicorn", "HTML2MD-API.main:html2md", "--host", "0.0.0.0", "--port", "5000"]

# If you have a proxy server, you can run it in the background here (optional)
# CMD ["python", "proxy_server.py"]
