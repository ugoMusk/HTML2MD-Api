#!/usr/bin/env python3
""" converter engine """
import os
import tempfile
import hashlib
import html2text
from requests_html import HTMLSession
import requests


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


def downloadUrl(url):
    """Scrape the web and convert HTML to Markdown"""
    session = HTMLSession()

    try:
        res = session.get(url)
        res.raise_for_status()
        res.encoding = "utf-8"
        body = res.text

        # Generate a unique hash for the URL to use as the filename
        url_hash = hashlib.md5(url.encode()).hexdigest()

        # Create a temporary directory to store files
        temp_dir = tempfile.mkdtemp()

        # Save the HTML content to a temporary file (for debugging purposes)
        html_file_path = os.path.join(temp_dir, f"{url_hash}.html")
        with open(html_file_path, mode="w", encoding="utf-8") as html_file:
            html_file.write(body)

        # Convert HTML to Markdown
        convertedMd = convertHtml2Markdown(body)

        return convertedMd, html_file_path

    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)

    return None, None


def main():
    """ entry point """
    print("engine build success!")

if __name__ == '__main__':
    main()
