#!/usr/bin/env python3
""" converter engine """

import html2text
import requests_html
import markdown

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


def downLoadUrl(url):
    """ scrab the web """
    pass

    
def main():
    """ entry point """
    print("engine build success!")
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
