#!/usr/bin/env python

# Call vendor to add the dependencies to the classpath
import vendor
vendor.add('lib')

# Import the Flask Framework
from flask import Flask, render_template, jsonify, request, url_for
app = Flask(__name__)

# For getting and parsing HTML
from urllib import quote_plus
from urllib2 import Request, urlopen
from bs4 import BeautifulSoup

subreddits = ["dankmemes", "circlejerk"]

@app.route("/")
def index_route():
	q = request.args.get("q")
	if q:
		return jsonify(tags=list(search_reddit_img(q)))
	else:
		return render_template("index.html")

def get_page(url):
	request = Request(url)
	request.add_header('User-Agent','Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)')
	response = urlopen(request)
	html = response.read()
	response.close()
	return html

def search_reddit_img(q):
	# Set of hashes for the results found.
	# This is used to avoid repeated results.
	hashes = set()

	for subreddit in subreddits:
		html = get_page("https://www.reddit.com/r/" + subreddit + "/search?q=" + quote_plus(q) + "&restrict_sr=on&sort=relevance&t=all")
		soup = BeautifulSoup(html, "html.parser")
		anchors = soup.findAll('a')
		for a in anchors:
			# Get the URL from the anchor tag.
			try:
			    link = a['href']
			except KeyError:
			    continue

			# Only accept imgur links for now
			is_img = link.startswith("http://i.imgur.com/")
			is_link_to_img = link.startswith("http://imgur.com/")
			if is_link_to_img:
				link = "http://i.imgur.com/" + link[17:] + ".png"
			elif is_img:
				pass
			else:
				continue

			# Discard repeated results.
			h = hash(link)
			if h in hashes:
			    continue
			hashes.add(h)

			yield link

if __name__ == '__main__':
	app.run()