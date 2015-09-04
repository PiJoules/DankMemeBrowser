#!/usr/bin/env python

# Import the Flask Framework
from flask import Flask, render_template, jsonify, request, url_for
app = Flask(__name__)

import search

@app.route("/")
def index_route():
	q = request.args.get("q")
	if q:
		tags = list(search.search_reddit_img(q))
		return render_template("index.html", tags=tags)
	else:
		return render_template("index.html", tags=[])

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500