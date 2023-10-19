# Use mysql docker image
FROM mysql:8.0

# Copy the sql initialization script to the docker-entrypoint-initdb.d directory
COPY init.sql /docker-entrypoint-initdb.d/

# Expose the ports used by your application
EXPOSE 3306 8080