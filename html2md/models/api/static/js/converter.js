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
/*
function showGitBtn(){
    // Get the element by it IDs
    const element = document.getElementById("postToGitHubBtn");
    let dis = window.getComputedStyle(element).getPropertyValue("display");
    if (dis !== 'block'){
	element.style.display = 'block'
    }
}*/
/*
// Get the form element
var form = document.getElementById("form");

// Add a submit event listener
form.addEventListener("submit", function(event) {
    // Prevent the default form submission
    event.preventDefault();

    // Get the form data
    var data = new FormData(form);

    // Send the data using fetch
    fetch("/convert", {
	method: "POST", // The request method
	body: data, // The request body
    })
    // Handle the response
	.then(function(response) {
	    // Check if the response is ok
	    if (response.ok) {
		// Extract the response body as text
		return response.text();
	    } else {
		// Throw an error
		throw new Error("Something went wrong");
	    }
	})
    // Handle the response body
	.then(function(text) {
	    // Do something with the text
	    // For example, show a message
	    document.getElementById("message").textContent = text;

	    // Get the element by its ID
	    const element = document.getElementById("postToGitHubBtn");
	    let dis = window.getComputedStyle(element).getPropertyValue("display");
	    if (dis !== "block") {
		element.style.display = "block";
	    }
	})
    // Handle any errors
	.catch(function(error) {
	    // Log the error
	    console.error(error);
	});
});
*/
function showGitForm(){
    // Get the element by its ID
    const gitHubBtn = document.getElementById("postToGitHubBtn");
    gitHubBtn.addEventListener("click", function(){
	var githubForm = document.getElementById("github-inputs");
	let dis = window.getComputedStyle(githubForm).getPropertyValue("display");
	if (dis !== "block") {
            githubForm.style.display = "block";
	    githubForm.scrollIntoView();
	}
    });
}
showGitForm();
