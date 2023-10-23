import base64
import requests


def get_current_file_sha(repo_owner, repo_name, file_path_in_repo, github_token):
    api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path_in_repo}"
    response = requests.get(api_url, headers={"Authorization": f"Bearer {github_token}"})


    if response.status_code == 200:
        file_info = response.json()
        return file_info.get("sha")
    else:
        print(f"Failed to fetch file info from GitHub. Status code: {response.status_code}")
        return None


def upload_file_to_github(file_path, repo_owner, repo_name, file_path_in_repo, github_token):
    try:
        # Read the file content and encode it to base64
        with open(file_path, 'rb') as file_content:
            base64_content = base64.b64encode(file_content.read()).decode()


        # Get the current SHA of the file from GitHub
        
        json_payload = {
            "message": "Upload file",
            "content": base64_content,
            # "sha": current_sha,  # Include the current SHA in the payload
        }


        # GitHub API endpoint
        api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path_in_repo}"


        # Upload the file to GitHub using requests library
        response = requests.put(api_url, json=json_payload, headers={"Authorization": f"Bearer {github_token}"})


        if response.status_code == 201:
                print("File uploaded to GitHub successfully.")
        else:
            print(f"Failed to upload file to GitHub. Status code: {response.status_code}")
            print(response.content)  # Print response content for debugging

    except Exception as e:
        print(f"Error: {e}")


# Example usage
file_path = "scarb.md"
repo_owner = "Sue609"
repo_name = "test"
file_path_in_repo = "README.md"
github_token = "GITHUB_TOKEN"


# Call the function to upload the file to GitHub
# upload_file_to_github(file_path, repo_owner, repo_name, file_path_in_repo, github_token)
