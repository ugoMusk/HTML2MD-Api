#!/usr/bin/env python3
"""
module defining our api endpoints
"""

from flask import Flask
from engine import downloadUrl, convertHtml2Markdown


app = Flask(__name__)


@app.route("/convert/url", methods=['GET'], strict_slashes=False)
def getMarkdown():
    """ 
    route method to parse html to markdown
    """
    res = downloadUrl("https://www.geeksforgeeks.org/flask-http-methods-handle-get-post-requests/")
    
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


    
if __name__ == "__main__":
    app.run()