from urllib.request import urlopen
from bs4 import BeautifulSoup


url = "http://collemc.people.si.umich.edu/data/bshw3StarterFile.html"
html = urlopen(url).read()

soup = BeautifulSoup(html, "html.parser")
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.


students = soup.find_all(class_="menu")
print (type(students))

students = soup.fina_all(class_="menu__item is-lead first lead menu-mlid")

for header in students:
	for x in header.find_all('a'):
		print (header)
		# if "Student" in x.get('href'):







