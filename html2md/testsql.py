# Import the sqlalchemy module
import os
import sqlalchemy
from sqlalchemy.orm import sessionmaker
import subprocess

mysqlRootUser = os.environ.get("MYSQL_ROOT_USER")
mysqlRootPassword = os.environ.get("MYSQL_ROOT_PASSWORD")

ip = subprocess.check_output(["docker", "inspect", "-f", "{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}", "html2mddb"]).decode("utf-8").strip()
print(f"database ip address: {ip}")

# Create an engine to connect to the MySQL database using the user credentials and the host name of the MySQL container
engine = sqlalchemy.create_engine("mysql+mysqlconnector://{}:{}@{}/html2md".format(mysqlRootUser, mysqlRootPassword, ip))

    
Session = sessionmaker(bind=engine)
session = Session()

# Run some queries on the database using a connection object
with session.connection() as conn:
    result = conn.execute(sqlalchemy.text('CREATE TABLE IF NOT EXISTS newT(id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), email VARCHAR(255));'))
    # Use rowcount instead of fetchall to get the number of rows affected
    print(result.rowcount)


    with session.connection() as conn:
        result = conn.execute(sqlalchemy.text("INSERT INTO newT(username, email) VALUES('ugosamsue', 'blablabla@devs.tech');"))
        session.commit()
        # Use rowcount instead of fetchall to get the number of rows affected
        print(result.rowcount)
