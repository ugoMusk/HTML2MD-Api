#!/usr/bin/env python3
"""
module defining our api endpoints
"""
import os
import sys
modelPath = os.path.abspath("../../models")
sys.path.append(modelPath)
from flask import Flask, jsonify, send_file
from engine.engine import downloadUrl, convertHtml2Markdown
from storage.cookies import *

app = Flask(__name__)


@app.route("/convert/url/<path:userUrl>", methods=['GET'], strict_slashes=False)
def getMarkdown(userUrl):
    """ 
    route method to parse html to markdown
    """
    res = downloadUrl(userUrl)
    
    return res


@app.route("/convert", methods=['GET'], strict_slashes=False)
def convertMarkdown():
    """ 
    route method to parse html to markdown
    """
    with open("scrab.html", mode="r", encoding="utf-8") as htmlFile:
        html = htmlFile.read()

    res = convertHtml2Markdown(html)
    
    return res


@app.route("/download", methods=['GET'], strict_slashes=False)
def downloadFile():
    """
    specify the path to the file to download
    """
    filePath = '/home/samke/HTML2MD-Api/html2md/models/engine/scab.md'
    return send_file(filePath, as_attachment=True)

@app.route("/")
def setcookie_route():
    # set a cookie with key "name" and value "Alice"
    return cookies.set_cookie()

@app.route("/getcookie")
def getcookie_route():
    # get a cookie with key "name"
    return cookies.get_cookie("name")

@app.route("/deletecookie")
def deletecookie_route():
    # delete a cookie with key "name"
    return cookies.delete_cookie("name")


if __name__ == "__main__":
    app.run()
