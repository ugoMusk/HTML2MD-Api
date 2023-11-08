#!/usr/bin/env python3
"""
module defining our api endpoints
"""
import os
import sys
modelPath = os.path.abspath("../../models")
sys.path.append(modelPath)
from flask import Flask, jsonify, send_file, render_template, url_for, request
from engine.engine import downloadUrl, convertHtml2Markdown
from storage import cookies
from flask_cors import CORS
import requests
import base64

app = Flask(__name__)

CORS(app)

@app.route("/convert/url/", methods=['GET'], strict_slashes=False)
def handleMissingURL():
    return "Error: No URL provided."

@app.route("/convert/url/<path:userUrl>", methods=['GET'], strict_slashes=False)

#@app.route("/convert/url/<path:userUrl>", methods=['GET'], strict_slashes=False)
def getMarkdown(userUrl):
    """ 
    route method to parse html to markdown
    """
    convertedMd, html_file_path = downloadUrl(userUrl)
    if convertedMd:
        return convertedMd
    else:
        return "Error occurred during conversion", 500



@app.route("/convert", methods=['POST'], strict_slashes=False)
def convert():
    try:
        data = request.get_json()
        userHtml = data.get('userHtml', '')
        convertedMD = convertHtml2Markdown(userHtml)
        return convertedMD
    except Exception as e:
        print(f"Error occurred: {e}")
        return "Error occurred during conversion"


@app.route('/upload', methods=['POST'])
def upload_to_github():
    try:
        data = request.get_json()
        markdown_content = data.get('file_content')
        repo_owner = data.get('repo_owner')
        repo_name = data.get('repo_name')
        file_path_in_repo = data.get('file_path_in_repo')
        github_token = data.get('github_token')

        base64_content = base64.b64encode(markdown_content.encode()).decode()

        json_payload = {
            "message": "Upload file",
            "content": base64_content,
        }

        api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path_in_repo}"

        response = requests.put(api_url, json=json_payload, headers={"Authorization": f"Bearer {github_token}"})

        if response.status_code == 201:
            return jsonify({"message": "File uploaded to GitHub successfully."}), 201
        else:
            return jsonify({"error": f"Failed to upload file to GitHub. Status code: {response.status_code}"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500
        

@app.route("/download", methods=['GET'], strict_slashes=False)
def downloadFile():
    """
    specify the path to the file to download
    """
    filePath = '/mnt/c/Users/Susan/Desktop/html2md-api/HTML2MD-Api/html2md/models/api/scrab.md'
    return send_file(filePath, as_attachment=True)

@app.route("/")
def setcookie_route():
    # set a cookie with key "name" and value "Alice"
    #return cookies.setCookie()
    return render_template("rapid.html")

@app.route("/getcookie")
def getcookie_route():
    # get a cookie with key "name"
    return cookies.getCookie("name")

@app.route("/deletecookie")
def deletecookie_route():
    # delete a cookie with key "name"
    return cookies.deleteCookie("name")


if __name__ == "__main__":
    app.run(debug=True)
