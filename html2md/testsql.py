# Import the sqlalchemy module
import sqlalchemy

# Create an engine to connect to the MySQL database using the user credentials and the host name of the MySQL container
engine = sqlalchemy.create_engine("mysql+psycopg2://$MYSQL_USER:MYSQL_PASSWORD@mysql-html2md/html2md")

# Run some queries on the database using a connection object
with engine.connect() as conn:
    result = conn.execute("SHOW TABLES;")
    print(result.fetchall())
