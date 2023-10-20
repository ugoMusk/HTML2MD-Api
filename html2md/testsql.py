# Import the sqlalchemy module
import sqlalchemy
import subprocess


ip = subprocess.check_output(["docker", "inspect", "-f", "{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}", "html2mddb"]).decode("utf-8").strip()
print(f"database ip address: {ip}")
# Create an engine to connect to the MySQL database using the user credentials and the host name of the MySQL container
engine = sqlalchemy.create_engine("mysql+mysqldb://$MYSQL_USER:MYSQL_PASSWORD@{}/html2md".format(ip)

# Run some queries on the database using a connection object
with engine.connect() as conn:
    result = conn.execute("SHOW TABLES;")
    print(result.fetchall())
