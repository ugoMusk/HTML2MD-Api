#!/usr/bin/env python3
"""
module defining our api endpoints
"""
import os
import sys
modelPath = os.path.abspath("../../models")
sys.path.append(modelPath)
from flask import Flask, jsonify, send_file, render_template, url_for, redirect, request
from engine.engine import downloadUrl, convertHtml2Markdown
from storage import cookies
from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app)

@app.route("/convert/url", methods=['GET', 'POST'], strict_slashes=False)
def convertUrl():
    """ 
    route method to parse html to markdown
    """
    userUrl = request.form.get('name')
    if userUrl:
        res = downloadUrl(userUrl)
    else:
        res = "Your converted Markdown will appear here"
    return render_template('converturl.html', userUrl=userUrl, result=res)
    # return res

@app.route("/convert/html", methods=['GET', 'POST'], strict_slashes=False)
def convertHtml():
    """ 
    route method to parse html to markdown
    """
    userUrl = request.form.get('name')
    if userUrl:
        res = downloadUrl(userUrl)
    else:
        res = "Your converted Markdown will appear here"
    return render_template('converthtml.html', userUrl=userUrl, result=res)
    # return res

@app.route("/convert", methods=['GET', 'POST'], strict_slashes=False)
def convertMain():
    """ 
    route method to parse html to markdown
    """
    try:
        with open("scrab.html", mode="r", encoding="utf-8") as htmlFile:
            html = htmlFile.read()
    except FileNotFoundError:
        html = "<body>please provide valid html</body>"

    res = convertHtml2Markdown(html)
    
    return render_template('convert.html', result=res)
    # return res


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
    # set a cookie with key "name" and value "Alice"
    return render_template("home.html", cookies=cookies.setCookie())

@app.route("/getcookie")
def getCookieRoute():
    # get a cookie with key "name"
    return cookies.getCookie("name")

@app.route("/deletecookie")
def deleteCookieRoute():
    # delete a cookie with key "name"
    return cookies.deleteCookie("name")

@app.route("/redirect")
def redirecRoute(url):
    #Set a redirection path
    url = url_for(url)
    return redirect(url)

@app.route("/docs")
def docs():
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
