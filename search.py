# For getting and parsing HTML
from urllib import quote_plus
from urllib2 import Request, urlopen
from bs4 import BeautifulSoup

# Subreddits to search from
subreddits = ["dankmemes", "circlejerk"]


"""
Just get the html from a given url.
"""
def get_page(url):
	request = Request(url)
	request.add_header('User-Agent','Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)')
	response = urlopen(request)
	html = response.read()
	response.close()
	return html


"""
Get tags from various subreddits given a query.
"""
def search_reddit_img(q):
	# Set of hashes for the results found.
	# This is used to avoid repeated results.
	hashes = set()

	for subreddit in subreddits:
		html = get_page("https://www.reddit.com/r/" + subreddit + "/search?q=" + quote_plus(q) + "&restrict_sr=on&sort=relevance&t=all")
		soup = BeautifulSoup(html, "html.parser")
		anchors = soup.findAll('a')

		results = soup.findAll("div",{"class": "search-result"})

		for result in results:
			a = result.find("a",{"class": "search-link"})
			if not a:
				continue

			title = result.find("a",{"class": "search-title"}).string

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

			yield {
				"link": link,
				"title": title
			}