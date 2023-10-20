#!/usr/bin/env python3
""" converter engine """

import markdown
import mistune
import html2text

def convertHtml2(html):
    """
    converts thtml to markdown
    """
    text = html2text.html2text(html)
    return text

def convertMarkdown(markdwon):
    """method to convert html to markdown """
    md = markdown.Markdown(extensions=["markdown.extensions.extra", "markdown.extensions.codehilite"])
    htmlResult = md.convert(html)
    return htmlResult

def convertHtml(html):
    """ Method to convert html to markdown"""
    markdownResult = mistune.create_markdown(html)
    print(f"The converted string: {markdownResult}")
    return markdownResult


if __name__ == '__main__':
    htmlFilePath = "test.html"
    mdFilePath = "test.md"
    with open(htmlFilePath, mode="r", encoding="utf-8") as htmlFile:
        htmlFile = htmlFile.read()
    mdFile = convertHtml2(htmlFile)
    with open(mdFilePath, mode="w", encoding="utf-8") as md:
        try:
            md.write(mdFile)
        except FileNotFoundError:
            print(f"{mdFilePath} does not exist")
