#!/usr/bin/env python3
""" converter engine """
from flask import Flask, request, jsonify
import markdown

app = Flask(__name)


def convert_html_to_markdown(html):
    """method to convert html to markdown """
    md = markdown.Markdown(extensions=["markdown.extensions.extra", "markdown.extensions.codehilite"])
    markdown_result = md.convert(html)
    return markdown_result

@app.route('/convert', methods=['POST'])
def convert():
    """ route method to parse html to markdown"""
    content_type = request.headers.get('Content-Type')
    if content_type == 'text/plain':
        # If the content type is 'text/plain', treat the request data as text
        html_content = request.data.decode('utf-8')
    elif content_type == 'text/html':
        # If the content type is 'text/html', treat the request data as HTML
        html_content = request.data.decode('utf-8')
    elif content_type == 'application/json':
        # If the content type is 'application/json', expect a JSON payload
        data = request.get_json()
        if 'text' in data:
            html_content = data['text']
        elif 'link' in data:
            pass
        else:
            return jsonify({'error': 'Invalid JSON format'}), 400
    else:
        return jsonify({'error': 'Invalid Content-Type'}), 400
    markdown_result = convert_html_to_markdown(html_content)
    return jsonify({'markdown': markdown_result})
if __name__ == '__main__':
    app.run(localhost="127.0.0.1", port=5000, debug=False)
