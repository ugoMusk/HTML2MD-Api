# import modules
import os
import sys
modelPath = os.path.abspath("../../models")
sys.path.append(modelPath)
from proxyserver import access
from flask import Flask, request, make_response
from sqlalchemy import create_engine, Column, String, DateTime, Integer, LargeBinary, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
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
engine = create_engine(f"mysql://{app.config['MYSQL_USER']}:{app.config['MYSQL_PASSWORD']}@{app.config['MYSQL_HOST']}/{app.config['MYSQL_DB']}")
Base = declarative_base()

# define Cookie class
class Users(Base):
    __tablename__ = "users"
    Id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(String(255), nullable=True)
    cookieValue = Column(String(255))
    cookieExpires = Column(DateTime)
    # firstName = Column(String(128), nullable=True)
    # lastName = Column(String(128), nullable=True)
    # userName = Column(String(128), nullable=True)
    # userPass = Column(String(128), nullable=True)
    # visitCounts = Column(Integer, nullable=True)
    # apiKey = Column(String(255), nullable=True)
    # userFile = Column(LargeBinary, nullable=True)

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
        # self.userFile = args[9] or ""
        

# create table for cookies
Base.metadata.create_all(engine)

# create session
Session = sessionmaker(bind=engine)
session = Session()

# define function to generate cookie ID
def generateCookieId():
    cookieId = session.query(users).filter_by(cookieId).first()
    if cookieId:
        exit()
        return 0
    return str(uuid4())

cookieKey = "userId"
cookieValue = access.getUserIp()
# define function to set cookie
def setCookie(key=cookieKey, value=cookieValue):
    # create response object

    resp = make_response("Setting the cookie")
    # generate cookie ID
    cookieId = generateCookieId()
    # set cookie in browser with ID as value
    resp.set_cookie(key, cookieId)
    # get current time and add one day for expiration
    now = datetime.now()
    expires = now + timedelta(days=1)

    # result = session.query(users.name).filter(users.age > 20).all()
    # store cookie data in database with ID, value, and expiration
    cookie = Users(cookieId, value, expires)
    session.add(cookie)
    session.commit()
    return resp

# define function to get cookie
def getCookie(key):
    # get cookie ID from browser
    cookieId = request.cookies.get(key)
    if not cookieId:
        return "No cookie found"
    # get cookie value and expiration from database
    cookie = session.query(Users).filter_by(cookieId=cookieId).first()
    if not cookie:
        return "No cookie found"
    value = cookie.cookieValue
    expires = cookie.cookieExpires
    # check if cookie is expired
    now = datetime.now()
    if now > expires:
        return "Cookie expired"
    return f"Cookie value is {value}"

# define function to delete cookie
def deleteCookie(key):
    # get cookie ID from browser
    cookieId = request.cookies.get(key)
    if not cookieId:
        return "No cookie found"
    # create response object
    resp = make_response("Deleting the cookie")
    # delete cookie from browser
    resp.deleteCookie(key)
    # delete cookie from database
    session.query(Users).filter_by(cookieId=cookieId).delete()
    session.commit()
    return resp

if __name__ == "__main__":
    app.run()
