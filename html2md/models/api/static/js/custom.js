#!/usr/bin/env node

/***
                      (*)
 _   _ _____ __  __ _     ____  __  __ ____
| | | |_   _|  \/  | |   |___ \|  \/  |  _ \
| |_| | | | | |\/| | |     __) | |\/| | | | |
|  _  | | | | |  | | |___ / __/| |  | | |_| |
|_| |_| |_| |_|  |_|_____|_____|_|  |_|____/

 *     Styles for render_template.html
 */

//document.getElementById('redirectButton').addEventListener('click', function() {
// window.location.href = '/convert/url/';
//});

//var textarea = document.getElementById("outputTextarea");

//window.addEventListener("load", function() {
    // Call the clearValue function on the textarea
    //clearValue(textarea);
  //});

document.getElementById("convertButton").addEventListener("click", function() {
    var userUrl = document.getElementById("urlInput").value;
    fetch("/convert/url/<path:userUrl>" + encodeURIComponent(userUrl)).then(response => response.text()).then(data => {
        document.getElementById("outputTextarea").value = data;
    }).catch(error => {
        console.error("Error:", error);
    });
});

//function showValue() {
  //var x = document.getElementById("showMd");
  //if (x.style.display === "none") {
    //x.style.display = "block";
  //} else {
    //x.style.display = "none";
