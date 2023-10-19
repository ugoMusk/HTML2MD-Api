# Use mysql docker image
FROM mysql:8.0

# Copy the sql initialization script to the docker-entrypoint-initdb.d directory
COPY init.sql /docker-entrypoint-initdb.d/
COPY init.sql /home/
RUN chown mysql:mysql /home/init.sql

# Expose the ports used by your application
EXPOSE 3306 8080