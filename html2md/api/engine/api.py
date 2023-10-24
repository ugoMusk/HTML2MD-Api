import base64
import requests


def get_user_input():
    """
    Reads and accepts users input
    """
    file_path = input("Enter the path to the file you want to upload: ")
    repo_owner = input("Enter the GitHub repository owner: ")
    repo_name = input("Enter the GitHub repository name: ")
    file_path_in_repo = input("Enter the desired file name in the repository (including extension): ")
    github_token = input("Enter your GitHub token: ")
    return file_path, repo_owner, repo_name, file_path_in_repo, github_token


def upload_file_to_github(file_path, repo_owner, repo_name, file_path_in_repo, github_token):
    """
    Uploads file to github using github rest Api
    """
    try:
        with open(file_path, 'rb') as file_content:
            base64_content = base64.b64encode(file_content.read()).decode()

        json_payload = {
            "message": "Upload file",
            "content": base64_content,
        }

        api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path_in_repo}"

        response = requests.put(api_url, json=json_payload, headers={"Authorization": f"Bearer {github_token}"})

        if response.status_code == 201:
            print("File uploaded to GitHub successfully.")
        else:
            print(f"Failed to upload file to GitHub. Status code: {response.status_code}")
            print(response.content)

    except Exception as e:
        print(f"Error: {e}")

file_path, repo_owner, repo_name, file_path_in_repo, github_token = get_user_input()

upload_file_to_github(file_path, repo_owner, repo_name, file_path_in_repo, github_token)
