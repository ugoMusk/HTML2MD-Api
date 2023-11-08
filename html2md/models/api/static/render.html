<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTML to Markdown Converter</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f8f8fa;
            color: #234463;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            text-align: center;
            margin-top: 50px;
        }
        .input-container {
            display: flex;
            justify-content: space-between;
            margin-bottom: 20px;
        }
        .input-box {
            flex: 1;
            margin-right: 30px; /* Increased margin for space between text areas */
        }
        .output-box {
            flex: 1;
            margin-left: 30px; /* Increased margin for space between text areas */
        }
        .button {
            background-color: #007bff;
            color: #ffffff;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .button:hover {
            background-color: #003fb3;
        }
        .input-box textarea, .output-box textarea {
            width: 100%;
            height: 400px;
            font-size: 14px;
            padding: 10px;
            resize: none;
            border: 1px solid #ced4da;
            border-radius: 5px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            display: block;
            margin-bottom: 10px;
        }
        .clear-button {
            background-color: #dc3545;
            color: #ffffff;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .clear-button:hover {
            background-color: #bb2c3d;
        }
        .github-inputs input {
            margin-bottom: 10px;
            width: calc(100% - 20px);
            padding: 10px;
            font-size: 14px;
            border: 1px solid #ced4da;
            border-radius: 5px;
        }
        #urlInput {
            width: 50%; /* Adjust this value to set the initial width of the input field */
            max-width: 300px; /* Adjust this value to limit the maximum width of the input field */
            padding: 10px;
            margin-bottom: 20px;
            font-size: 18px;
    }
    </style>
</head>
<body>

    <div class="container">
        <h1>HTML to Markdown Converter</h1>
        <div class="input-container">
            <div class="input-box">
                <label for="urlInput">Enter URL:</label>
                <input type="text" id="urlInput" placeholder="Enter URL">
            </div>
        </div>
        <button id="convertButton" class="button">Convert</button>
        <div class="input-container">
            <div class="input-box">
                <label for="userHtml">Enter Raw HTML:</label>
                <textarea id="userHtml" placeholder="Enter HTML"></textarea>
                <button class="clear-button" id="clearHtmlButton">Clear HTML</button>
            </div>
            <div class="output-box">
                <label>Markdown:</label>
                <textarea id="outputTextarea" readonly></textarea>
            </div>
        </div>
        <button id="postToGitHubBtn" class="button">Post to GitHub</button>
        <div class="github-inputs">
            <input type="text" id="repoOwnerInput" placeholder="GitHub Repo Owner" required>
            <input type="text" id="repoNameInput" placeholder="GitHub Repo Name" required>
            <input type="text" id="filePathInput" placeholder="File Path in Repo" required>
            <input type="text" id="githubTokenInput" placeholder="GitHub Token" required>
        </div>
    </div>

    <script>
        document.getElementById("convertButton").addEventListener("click", function() {
            var userUrl = document.getElementById("urlInput").value; // Get URL from input box
            var userHtml = document.getElementById("userHtml").value;
    
            if (userUrl || userHtml) {
                var url = userUrl ? `/convert/url/${encodeURIComponent(userUrl)}` : "/convert";
                var requestBody = userUrl ? null : JSON.stringify({ userHtml: userHtml });
    
                fetch(url, {
                    method: userUrl ? "GET" : "POST",
                    body: requestBody,
                    headers: {
                        "Content-Type": userUrl ? "text/plain" : "application/json"
                    }
                })
                .then(response => response.text())
                .then(data => {
                    document.getElementById("outputTextarea").value = data;
                })
                .catch(error => {
                    console.error("Error:", error);
                });
            } else {
                console.error("No URL or HTML input provided.");
            }
        });

        document.getElementById("clearHtmlButton").addEventListener("click", function() {
            document.getElementById("userHtml").value = "";
        });
        document.getElementById("postToGitHubBtn").addEventListener("click", function() {
            var markdownContent = document.getElementById("outputTextarea").value;
            var repoOwner = document.getElementById("repoOwnerInput").value;
            var repoName = document.getElementById("repoNameInput").value;
            var filePathInRepo = document.getElementById("filePathInput").value;
            var githubToken = document.getElementById("githubTokenInput").value;

            if (markdownContent && repoOwner && repoName && filePathInRepo && githubToken) {
                fetch("/upload", {
                    method: "POST",
                    body: JSON.stringify({
                        file_content: markdownContent,
                        repo_owner: repoOwner,
                        repo_name: repoName,
                        file_path_in_repo: filePathInRepo,
                        github_token: githubToken
                    }),
                    headers: {
                        "Content-Type": "application/json"
                    }
                })
                .then(response => response.json())
                .then(data => {
                    alert(data.message); // Show success or error message to the user
                })
                .catch(error => {
                    console.error("Error:", error);
                    alert("Error occurred while posting to GitHub. Check console for details.");
                });
            } else {
                alert("Please provide all required information.");
            }
        });
    </script>
</body>
</html>