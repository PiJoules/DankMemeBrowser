#!/usr/bin/env python

# Call vendor to add the dependencies to the classpath
import vendor
vendor.add('lib')

# Import the Flask Framework
from flask import Flask, render_template, jsonify, request, url_for
app = Flask(__name__)

# Import google python module
from google import search

@app.route("/")
def index_route():
	q = request.args.get("q")
	if q:
		return jsonify(result=list(search(q,stop=10)))
	else:
		return render_template("index.html")

if __name__ == '__main__':
	app.run()