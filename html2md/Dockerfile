# Use an official Python runtime as a parent image
FROM python:3
FROM mysql:8.0

# Set the working directory inside the container
WORKDIR /html2md

# update distro and install pip
#RUN apt update && apt install python3-pip -y

# Copy the rest of the application code into the container at /html2md
COPY . /html2md/

# Copy the sql initialization script to the docker-entrypoint-initdb.d directory
COPY init.sql /docker-entrypoint-initdb.d/

# Expose the ports used by your application
EXPOSE 5000 8080

# Set environment variables if necessary (optional)

# Command to run the API server (adjust as per your project structure)
CMD ["uvicorn", "html2md.main:app", "--host", "0.0.0.0", "--port", "5000"]

# If you have a proxy server, you can run it in the background here (optional)
# CMD ["python", "proxy_server.py"]