#!/usr/bin/env python3
"""
module defining our api endpoints
"""
import os
import sys
modelPath = os.path.abspath("../../models")
sys.path.append(modelPath)
from flask import Flask, jsonify, send_file, render_template
from engine.engine import downloadUrl, convertHtml2Markdown
from storage import cookies
from flask_cors import CORS

app = Flask(__name__)

CORS(app)
@app.route("/convert/url/<userUrl>", methods=['GET'], strict_slashes=False)

#@app.route("/convert/url/<path:userUrl>", methods=['GET'], strict_slashes=False)
def getMarkdown(userUrl):
    """ 
    route method to parse html to markdown
    """
    print("Received URL:", userUrl)
    res = downloadUrl(userUrl)
    
    return render_template('render_temp.html', result=res)
    #return res


@app.route("/convert", methods=['GET'], strict_slashes=False)
def convertMarkdown():
    """ 
    route method to parse html to markdown
    """
    with open("scrab.html", mode="r", encoding="utf-8") as htmlFile:
        html = htmlFile.read()

    res = convertHtml2Markdown(html)
    
    # return render_template('render_temp.html', result=res)
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
    return cookies.setCookie()

@app.route("/getcookie")
def getcookie_route():
    # get a cookie with key "name"
    return cookies.getCookie("name")

@app.route("/deletecookie")
def deletecookie_route():
    # delete a cookie with key "name"
    return cookies.deleteCookie("name")


if __name__ == "__main__":
    app.run()
