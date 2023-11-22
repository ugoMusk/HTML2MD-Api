from flask import Flask, render_template, request
import requests
import base64


def uploadFileToGithub(filePath, repoOwner,
                       repoName, repoFilePath,
                       githubToken):
    try:
        # GitHub API endpoint to check if the file already exists
        apiUrl = f'https://api.github.com/repos/{repoOwner}/{repoName}/contents/{repoFilePath}.md'
        
        # Make a GET request to GitHub API to check if the file exists
        response = requests.get(
            apiUrl,
            headers={
                'Authorization': f'Bearer {githubToken}',
            },
        )
        
        if response.status_code == 200:
            # File exists, update the existing file
            existingFileData = response.json()
            sha = existingFileData['sha']
            
            commitData = {
                "message": "Update existing Markdown file",
                "content": base64.b64encode(filePath.encode()).decode(),
                # Encode content in base64
                "sha": sha,
            }
            
            updateResponse = requests.put(
                apiUrl,
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {githubToken}',
                },
                json=commitData
            )
            
            if updateResponse.status_code == 200:
                return updateResponse
            else:
                return updateResponse
            
        elif response.status_code == 404:
            # File doesn't exist, create a new file
            commitData = {
                "message": "Add new Markdown file",
                "content": base64.b64encode(filePath.encode()).decode(),  # Encode content in base64
            }
            createResponse = requests.put(
            apiUrl,
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {githubToken}',
                },
                json=commitData
            )
            
            if createResponse.status_code == 201:
                return createResponse
            else:
                return createResponse
            
        else:
            return response
            
    except Exception as e:
        return response
