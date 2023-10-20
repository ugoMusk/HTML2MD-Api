# Import the sqlalchemy module
import os
import sqlalchemy
import subprocess


mysqlRootUser = os.environ.get("MYSQL_ROOT_USER")
mysqlRootPassword = os.environ.get("MYSQL_ROOT_PASSWORD")

ip = subprocess.check_output(["docker", "inspect", "-f", "{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}", "html2mddb"]).decode("utf-8").strip()
print(f"database ip address: {ip}")
# Create an engine to connect to the MySQL database using the user credentials and the host name of the MySQL container
engine = sqlalchemy.create_engine("mysql+mysqldb://{}:{}@{}/html2md".format(mysqlRootUser, mysqlRootPassword, ip))

# Run some queries on the database using a connection object
with engine.connect() as conn:
    result = conn.execute(sqlalchemy.text('SHOW DATABASES;'))
    print(result.fetchall())
