document.getElementById("convertButton").addEventListener("click", function() {
    var userUrl = document.getElementById("urlInput").value;
    var userHtml = document.getElementById("htmlInput").value;

    fetch("/convert", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: `url=${encodeURIComponent(userUrl)}&html=${encodeURIComponent(userHtml)}`
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.text();
    })
    .then(data => {
        document.getElementById("outputTextarea").textContent = data;
    })
    .catch(error => {
        console.error("Error:", error);
    });
});
