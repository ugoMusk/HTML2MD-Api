#!/usr/bin/env python3
"""
module defining our api endpoints
"""
import os
import sys
import socket
modelPath = os.path.abspath("../../models")
sys.path.append(modelPath)
from proxyserver import access
from flask import Flask, jsonify, send_file, render_template, url_for, redirect, request, make_response
from engine.engine import downloadUrl, convertHtml2Markdown
from storage.cookies import updateUserFile, getUserFile, session, Users, setCookie
from flask_cors import CORS, cross_origin
from flask_compress import Compress
from  git_post import uploadFileToGithub
import json
import base64
import chardet
from datetime import datetime, timedelta
from sqlalchemy.exc import PendingRollbackError, IntegrityError

app = Flask(__name__)

compress = Compress()
compress.init_app(app)

CORS(app)

@app.route("/convert/url", methods=['GET', 'POST'], strict_slashes=False)
def convertUrl():
    """ 
    route method to parse html to markdown
    """
    userUrl = request.form.get('name')
    if userUrl:
        res = downloadUrl(userUrl)
        userFile = request.form.get('convertedMarkdown')
        updateUserFile(userFile)
    else:
        res = "Your converted Markdown will appear here"
    return render_template('converturl.html', userUrl=userUrl, result=res)
    # return res

@app.route("/convert/html", methods=['GET', 'POST'], strict_slashes=False)
def convertHtml():
    """ 
    route method to parse html to markdown
    """
    userHtml = request.form.get('userHtml')
    if userHtml:
        res = convertHtml2Markdown(userHtml)
        userFile = request.form.get('convertedMarkdown')
        updateUserFile(userFile)
    else:
        res = "Your converted Markdown will appear here"
    return render_template('converthtml.html', result=res)
    # return res

@app.route("/convert", methods=['GET', 'POST'], strict_slashes=False)
def convertMain():
    """ 
    route method to parse html to markdown
    """

    res = "converted markdown appears here"
    userIp = request.headers.get("X-Forwarded-For", request.remote_addr)
    if request.form.get('userUrl'):
        userInput = request.form.get('userUrl')
        try:
            res = downloadUrl(userInput)
            resDb = updateUserFile(res, userIp)
            gitBtn = "Post to github?"
        except Exception as e:
            res = f"{e}"
            resDb = f"Error {e}"
            gitBtn = f"{e}"
    elif request.form.get('userHtml'):
        userInput = request.form.get('userHtml')
        try:
            res = convertHtml2Markdown(userInput)
            resDb = updateUserFile(res, userIp)
            gitBtn = "Post to github?"
        except Exception as e:
            res = f"{e}"
            resDb = f"{e}"
            gitBtn = f"{e}"
    else:
        resDb = ''
        gitBtn = ''
    return render_template('convert.html', result=res, resultDb=resDb, resultBtn=gitBtn)

@app.route("/upload", methods=['GET', 'POST'], strict_slashes=False)
def postToGithub():
    """ upload converted markdown to user's github repository """

    filePath = getUserFile()
    repoOwner = request.form.get('repoOwner')
    repoName = request.form.get('repoName')
    repoFilePath = request.form.get('repoFilePath')
    githubToken = request.form.get('githubToken')

    res = uploadFileToGithub(filePath,
                              repoOwner,repoName,
                              repoFilePath,
                              githubToken)

    if res.status_code == 201 or res.status_code == 200:
       dictRes = f"Markdown posted to Github with status {res.status_code}"
    elif res.status_code == 404:
      dictRes = f"Github Repository doesn't exist or likely a typo in your github user name and or  repo name: error : {res.status_code}"
    elif res.status_code == 401:
      dictRes = f"Your PAT is either invalid or expired, you should likely  create a new one: error : {res.status_code}"
    else:
      dictRes = f"I'm not sure I understand what you're trying to do, please fill 'in' your details correctly: error : {res.status_code}"
    return render_template('convert.html', postRes=dictRes)
    
@app.route("/download", methods=['GET'], strict_slashes=False)
def downloadFile():
    """
    specify the path to the file to download
    """
    filePath = 'scab.md'
    try:
        with open(filePath, mode="r", encoding="utf-8") as dFile:
            mdFile = dFile.read()
            sendFile = send_file(mdFile, as_attachment=True)
    except FileNotFoundError:
        sendFile = (f"{filePath} does not exists")
    return sendFile

@app.route("/")
def setCookieRoute():
    """ home route, application entry point """
    # get client's ip address
    ipAddress = request.headers.get("X-Forwarded-For", request.remote_addr)
    # set a cookie with key cookieKey and value "cookieValue"
    cookieKey = "userId"
    cookieValue = ipAddress
    resp = setCookie(cookieKey, cookieValue)
    if resp == "None":
        # create a response object from the view function's return value
        resp = make_response("Setting cookie again")
        resp.set_header('Access-Control-Allow-Origin', request.origin)
        # set the cookie on the response object
        resp.set_cookie(cookieKey, cookieValue, expires=datetime.utcnow() + timedelta(days=7))
    return render_template("home.html")

@app.route("/getcookie")
def getCookieRoute():
    """ get a cookie with key 'name' """
    return cookies.getCookie("name")

@app.route("/deletecookie")
def deleteCookieRoute():
    """ delete a cookie with key 'name' """
    return cookies.deleteCookie("name")

@app.route("/redirect")
def redirecRoute(url):
    """ set a redirection path """
    url = url_for(url)
    return redirect(url)

@app.route("/docs")
def docsPage():
    """ docs page """
    return render_template("docs.html")

@app.route("/archive", methods=['POST'], strict_slashes=False)
def archiveMarkdown():
    """
    perform update operation on database with 
    converted markdown
    """
    return True


if __name__ == "__main__":
    app.run()
