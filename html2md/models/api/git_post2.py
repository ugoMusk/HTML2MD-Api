import base64
import requests


def getCurrentSha(repoOwner, repoName,
                         repoFilePath,
                         githubToken):
    apiUrl = f"https://api.github.com/\
    repos/{repoOwner}/{repoName}/\
    contents/{repoFilePath}"
    response = requests.get(
        apiUrl, headers={"Authorization": f"Bearer {githubToken}"}
    )

    if response.status_code == 200:
        fileInfo = response.json()
        return fileInfo.get("sha")
    else:
        print(
            f"Failed to fetch file info from\
        GitHub. Status code:\
        {response.status_code}"
        )
        return None


def uploadFileToGithub(
    filePath, repoOwner, repoName, repoFilePath, githubToken
):
    try:
        # Read the file content and encode it to base64
        with open(filePath, "rb") as fileContent:
            base64Content = base64.b64encode(fileContent.read()).decode()

        # Get the current SHA of the file from GitHub
        currentSha = getCurrentSha(
            repoOwner, repoName, repoFilePath, githubToken
        )

        if currentSha:
            json_payload = {
                "message": "Upload file",
                "content": base64Content,
                "sha": currentSha,  # Include the current SHA in the payload
            }

            # GitHub API endpoint
            apiUrl = f"https://api.github.com/repos/{repoOwner}/{repoName}/\
contents/{repoFilePath}"

            # Upload the file to GitHub using requests library
            response = requests.put(
                apiUrl,
                json=json_payload,
                headers={"Authorization": f"Bearer {githubToken}"},
            )

            if response.status_code == 201:
                print("File uploaded to GitHub successfully.")
            else:
                print(
                    f"Failed to upload file to\
                GitHub. Status code:\
                {response.status_code}"
                )
                print(response.content)  # Print response content for debugging

        else:
            print("Failed to obtain current SHA of the file from GitHub.")

    except Exception as e:
        print(f"Error: {e}")
        
