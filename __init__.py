#!/usr/bin/env python

# Call vendor to add the dependencies to the classpath
import vendor
vendor.add('lib')

# Import the Flask Framework
from flask import Flask, render_template, jsonify, request, url_for
app = Flask(__name__)

import search

@app.route("/")
def index_route():
	q = request.args.get("q")
	if q:
		tags = list(search.search_reddit_img(q))
		return render_template("rows.html", tags=tags)
	else:
		return render_template("index.html")

if __name__ == '__main__':
	app.run()