from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup


url = "http://collemc.people.si.umich.edu/data/bshw3StarterFile.html"
r = requests.get(url) 
soup = BeautifulSoup(r.text, "lxml") 
f = open("new.html", "w")

soup_string = str(soup)
# print (soup_string)
f = f.write(soup_string)

tags = soup.find_all("div", {"class":"menu-block-wrapper menu-block-1 menu-name-main-menu parent-mlid-0 menu-level-2"})

for t in tags:
	#if "menu__item is-leaf leaf menu-mlid" in t:
	#print (t)
	for i in t.find_all('li'):
		# print (i)
		for x in i.find_all('a'):
			x_href = x.get("href")
			if "student" in x_href:
				print (x_href.replace("students", "AMAZING Student"))
				


# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.




