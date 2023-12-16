#!/usr/bin/env python3
import os
import sys
modelPath = os.path.abspath("../../models")
sys.path.append(modelPath)
from flask import Flask, request, make_response
from sqlalchemy import (
    create_engine,
    Column,
    String,
    DateTime,
    Integer,
    LargeBinary,
    Table,
    MetaData,
    select,
    VARCHAR

)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import PendingRollbackError, IntegrityError
from proxyserver import access
from datetime import datetime, timedelta
from uuid import uuid4

dbHost = os.environ.get("MYSQL_HOST")
dbUser = os.environ.get("MYSQL_USER")
dbPass = os.environ.get("MYSQL_PASSWORD")

# create app and configure MySQL
app = Flask(__name__)
app.config["MYSQL_HOST"] = dbHost
app.config["MYSQL_USER"] = dbUser
app.config["MYSQL_PASSWORD"] = dbPass
app.config["MYSQL_DB"] = "html2md"

# create engine and base class
engine = create_engine(
    f"mysql://{app.config['MYSQL_USER']}:{app.config['MYSQL_PASSWORD']}@{app.config['MYSQL_HOST']}/{app.config['MYSQL_DB']}?charset=utf8mb4"
)
Base = declarative_base()


# define Cookie class
class Users(Base):
    __tablename__ = "users"
    Id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(String(255), nullable=True)
    cookieValue = Column(String(255), unique=True)
    cookieExpires = Column(DateTime)
    # firstName = Column(String(128), nullable=True)
    # lastName = Column(String(128), nullable=True)
    # userName = Column(String(128), nullable=True)
    # userPass = Column(String(128), nullable=True)
    # visitCounts = Column(Integer, nullable=True)
    # apiKey = Column(String(255), nullable=True)
    userFile = Column(VARCHAR(7800), nullable=True)

    def __init__(self, *args):
        self.userId = args[0]
        self.cookieValue = args[1]
        self.cookieExpires = args[2]
        # self.firstName = args[3] or ""
        # self.lastName = args[4] or ""
        # self.userName = args[5] or ""
        # self.userPass = args[6] or ""
        # self.visitCounts = args[7] or 0
        # self.apiKey = args[8] or ""
        self.userFile = args[3]


# create table for cookies
Base.metadata.create_all(engine)

metadata = MetaData()
# create session
Session = sessionmaker(bind=engine)
session = Session()

userFile = " "
users = Table(
    "users",
    metadata,
    Column("userId", String(255)),
    Column("cookieValue", String(255), unique=True),
    Column("cookieExpires", DateTime),
    Column("userFile", String(255))
)


# define function to generate cookie ID
def generateCookieId():
    return str(uuid4())


# define function to set cookie
def setCookie(cookieKey, cookieValue):
    # create response object

    resp = make_response("Setting the cookie")
    # generate cookie ID
    # cookieId = generateCookieId()
    # set cookie in browser with ID as value
    resp.set_cookie(cookieKey, cookieValue)
    # get current time and add one day for expiration
    now = datetime.now()
    expires = now + timedelta(days=1)
    try:
        # result = session.query(users.name).filter(users.age > 20).all()
        # store cookie data in database with ID, value, and expiration
        userInfo = Users(cookieKey, cookieValue, expires, userFile)
        session.add(userInfo)
        session.commit()
    except IntegrityError:
        session.rollback()
    return resp

# define function to get cookie
def getCookie(key):
    # get cookie ID from browser
    cookieValue = request.cookies.get(key)
    if not cookieValue:
        return "No cookie found"
    # get cookie value and expiration from database
    user = session.query(Users).filter_by(cookieValue=cookieValue).first()
    if not user:
        return "No cookie found"
    value = user.cookieValue
    expires = user.cookieExpires
    # check if cookie is expired
    now = datetime.now()
    if now > expires:
        return "Cookie expired"
    return f"Cookie value is {value}"


# define function to delete cookie
def deleteCookie(key):
    # get cookie ID from browser
    cookieValue = request.cookies.get(key)
    if not cookieValue:
        return "No cookie found"
    # create response object
    resp = make_response("Deleting the cookie")
    # delete cookie from browser
    resp.deleteCookie(key)
    # delete cookie from database
    session.query(Users).filter_by(cookieId=cookieId).delete()
    session.commit()
    return resp


def updateUserFile(markdown, userIp):
    """
    updates the user's file in database
    usage: updateUserFile(markdown, userIp)
    """
    try:
        # Check if the user already exists
        user = session.query(Users).filter_by(cookieValue=userIp).first()

        if user:
            # Update the existing user's file content
            user.userFile = markdown
            session.commit()
            ret = f"like what you see? We can help post to any repo of your choice on github, scroll to bottom to access the feature!"
        else:
            # Call setCookies
            setCookie("userId", userIp)
            ret = f"record set successful"

    except Exception as e:
        # Handle exceptions, rollback changes, and log the error
        session.rollback()
        # ret = f"Error: {e}"
        ret = f"something went wrong: error : {e}"
    finally:
        # Close the session
        session.close()
    return ret

def getUserFile():
    """ gets the value of a user file column in database """

    try:
        # Check if the user already exists in the db
        user = session.query(Users).filter_by(cookieValue=cookieValue).first()
        if user:
            userFile = user.userFile
        else:
            userFile = f"you do not have a record in our database, use one of our converter options to get started!"
    except Exception as e:
        userFile = f"{e}"
    return userFile

if __name__ == "__main__":
    app.run()
