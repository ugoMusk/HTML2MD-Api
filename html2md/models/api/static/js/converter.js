/* document.getElementById("convertButton").addEventListener("click", function() {
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

var postBtn = document.getElementById('postToGitHuBtn');

document.getElementById("convertBtn").addEventListener("click", function() {
    postBtn.style.display = "block";
}
*/


// Get the element and the button by their IDs
var element = document.getElementById("postToGitHubBtn");
var button = document.getElementById("convertBtn");

// Add a click event listener to the button
button.addEventListener("click", function() {
  // Check the current value of the display property
  if (element.style.display === "none") {
    // If the element is hidden, show it
    element.style.display = "inline";
  } else {
    // If the element is visible, hide it
    element.style.display = "none";
  }
});
