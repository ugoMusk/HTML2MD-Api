#!/usr/bin/env python3
"""
module defining our api endpoints
"""

from flask import Flask, jsonify, send_file
from engine import downloadUrl, convertHtml2Markdown


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

@app.route('/')
def getClientIp():
    """
    retrieves client's Ip address
    """
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        clientIp = request.environ['REMOTE_ADDR']
    else:
        clientIp = request.environ['HTTP_X_FORWARDED_FOR']
    return f"Client's IP address: {client_ip}"

    
if __name__ == "__main__":
    app.run()
