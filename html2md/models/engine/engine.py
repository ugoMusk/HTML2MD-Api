#!/usr/bin/env python3
""" converter engine """

import html2text
import requests
import requests_file
import markdown
import chardet

def convertHtml2Markdown(html):
    """ converts html to markdown format """
    text = html2text.HTML2Text()
    text.ignore_links = True
    markdown = text.handle(html)
    return markdown

def convertMarkdown2Html(markdown):
    """ convert markdown to html """
    md = markdown.Markdown(extensions=["markdown.extensions.extra", "markdown.extensions.codehilite"])
    htmlResult = md.convert(markdown)
    return htmlResult


""" def downloadUrl(url):
    #scrab the web
    session = HTMLSession()
    url = url
    res = session.get(url)
    res.encoding = "utf-8"
    body = res.text

    # path2Html = "scrab.html"
    # path2Md = "scrab.md"

    with open(path2Html, mode="w", encoding="utf-8") as scrabFile:
        try:
            scrabFile.write(body)
        except Exception as e:
            print(e)
    with open(path2Html, mode="r", encoding="utf-8") as scrabFile:
        htmlFile = scrabFile.read()
    with open(path2Md, mode="w", encoding="utf-8") as scrabMd:
        try:
            convertedMd = convertHtml2Markdown(htmlFile)
            scrabMd.write(convertedMd)
        except FileNotFoundError:
            print(f"{scrabMd} Not Found!")
    return convertedMd """
def downloadUrl(url):
    # Send a GET request to url
    response = requests.get(url)
    encoding = chardet.detect(response.content)['encoding']
    body = response.content.decode(encoding)
    # Deacode reponse to text and assign to variable
    # encoding = chardet.detect(response.content)['encoding']

    # body = response.content.decode(encoding)
    
    """ path2Html = "scrab.html"
    path2Md = "scrab.md"

    try:
        with open(path2Html, mode="w", encoding="utf-8") as scrabFile:
            try:
                scrabFile.write(body)
            except Exception as e:
                print(e)
    except FileNotFoundError:
        print(f"{path2Html} not found")
    try:    
        with open(path2Html, mode="r", encoding="utf-8") as scrabFile:
            htmlFile = scrabFile.read()
            with open(path2Md, mode="w", encoding="utf-8") as scrabMd:
                try:
                    convertedMd = convertHtml2Markdown(htmlFile)
                    scrabMd.write(convertedMd)
                except FileNotFoundError:
                    print(f"{scrabMd} Not Found!")
                    return convertedMd
    except FileNotFoundError:
        print(f"{path2Html} not found")
    """
    convertedMd = convertHtml2Markdown(body)
    return convertedMd
    
def main():
    """ entry point """
    print("engine build success!")
    #downloadUrl("https://www.geeksforgeeks.org/flask-http-methods-handle-get-post-requests/")
    # htmlFilePath = "html2md/api/engine/file_resource/test.html"
    # mdFilePath = "html2md/api/engine/file_resource/test.md"
    #with open(htmlFilePath, mode="r", encoding="utf-8") as htmlFile:
        # htmlFile = htmlFile.read()
    # mdFile = convertHtml2Markdown(htmlFile)
    #with open(mdFilePath, mode="w", encoding="utf-8") as md:
        # try:
            # md.write(mdFile)
        # except FileNotFoundError:
            #print(f"{mdFilePath} does not exist")


if __name__ == '__main__':
    main()
