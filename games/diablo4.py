import urllib
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

class Diablo4():

	def __init__(self):
		self.name = "Diablo 4"
		self.names = ["diablo"]
		self.patch = {"title": None, "url": None, "desc": None, "image": None}
		self.color = 16777215
		self.thumbnail = "https://imgur.com/a/gkPGVMh"

	def get_patch_info(self):

		# Source Diablo 4 Page
		try:
			request = Request("https://news.blizzard.com/en-us/diablo4/23964909/diablo-iv-patch-notes", headers={'User-Agent': 'Mozilla/5.0'})
			source = urlopen(request).read()
			bsoup = soup(source, "html.parser")
		except:
			raise Exception("Couldn't connect to " + self.name + "'s website.")

		try:
			side_div = bsoup.findAll("div",{"class":"Pane-content"})
		except:
			raise Exception("Error retrieving Pane-content")

		# Gets Overwatch's patch title.
		try:
			self.patch["title"] = side_div[0].ResponsiveBlogs
			if self.patch["title"] is None:
				raise Exception("Could not find " + self.name + " title.")
		except:
			raise Exception("Error retrieving " + self.name + " title.")

		# Gets Overwatch's patch url.
		try:
			self.patch["url"] = "https://news.blizzard.com/en-us/diablo4/23964909/diablo-iv-patch-notes" + side_div[0].ul.li.a["href"]
			if self.patch["url"] is None:
				raise Exception("Could not find " + self.name + " url.")
		except:
			raise Exception("Error retrieving " + self.name + " url.")

		# Gets Overwatch's patch description.
		try:
			calloutbox_div = bsoup.findAll("div",{"class":"ResponsiveBlogs"})
			desc = ""
			for div in calloutbox_div:
				try:
					desc = desc + div.p.text.body + "\n"
				except AttributeError:
					pass
			self.patch["desc"] = desc
			if self.patch["desc"] is "":
				raise Exception("Could not find " + self.name + " description.")
		except:
			raise Exception("Error retrieving " + self.name + " description.")

	def find_between(self, s, first, last):
		start = s.index(first) + len(first)
		end = s.index(last, start)
		return s[start:end]