import vendor
vendor.add("lib")

import requests
import json
import sys
import re


"""
Get the json from https://www.reddit.com/user/imgurtranscriber.json?sort=top
"""
def get_json(sort="top", limit=1000):
	url = "https://www.reddit.com/user/imgurtranscriber.json"
	payload = {
		"sort": "top",
		"limit": limit
	}
	r = requests.get(url, params=payload)
	if r.status_code != requests.codes.ok:
		print r.url
		print r.json()
		sys.exit()
	return r.json()


"""
Check if the image is valid.
The body will contain "Error:139" if it is invalid.
"""
def is_valid_image(body):
	return not "error:139" in body.lower()


"""
Extract the top text from the post body.
"""
def extract_top_text(body):
	m = re.search(r"\*\*\*Top:\*\*\*\s*\*([^*]+)\*", body)
	return m.group(1)


"""
Extract the bottom text from the post body.
"""
def extract_bottom_text(body):
	pass


"""
Parse the json.
Get the:
1. body
2. name (unique id for each post)
3. link_title
4. link_url (image)

Format example given in https://www.reddit.com/user/imgurtranscriber.json?sort=top
"""
def parse_json(obj):
	latest_post = obj["data"]["after"]
	posts = obj["data"]["children"]
	filtered_posts = []

	for post in posts:
		data = post["data"]
		# Make sure these are included just in case
		if not ("body" in data and "name" in data and "link_title" in data and "link_url" in data):
			continue

		body = data["body"]
		if not is_valid_image(body):
			continue
		print extract_top_text(body)
		sys.exit()



"""
Pretty print json (for testing)
"""
def pretty_print_json(obj):
	print json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': '))


if __name__ == "__main__":
	reddit_json = get_json()
	#pretty_print_json(reddit_json)
	parse_json(reddit_json)