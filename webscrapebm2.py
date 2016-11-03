from bs4 import BeautifulSoup

import requests, json

cats = []
#offset = 0

#while offset <= 85:


url = "https://www.brooklynmuseum.org/opencollection/search?keyword=feline"

photo_page = requests.get(url)

page_html = photo_page.text

soup = BeautifulSoup(page_html, "html.parser")

div = soup.find("div", attrs = {"class": "row results-category"})

all_div = soup.find_all("div", attrs = {"class": "row"})

for a_link in all_div:

	title_a = a_link.find("a")
	if title_a != None:

		cats_dict = a_link.find("span")
		if cats_dict != None:
			cats.append({"title":title_a.text, "moreinfo":cats_dict.text})


	#offset = offset + 1
	#print("There are now " + str(len(cats)))

with open('bm_cats.json', 'w') as f:
	f.write(json.dumps(cats,indent=4))
