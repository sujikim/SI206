from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests


#Making a request to Colleen's UMSI website
url = "http://collemc.people.si.umich.edu/data/bshw3StarterFile.html"
r = requests.get(url) 
#Using BeautifulSoup to turn the requested data into a soup object
soup = BeautifulSoup(r.text, "lxml") 
#Creating my own html file
f = open("new.html", "w")

#Turning the html file into string format
pretty_soup = soup.prettify()

#Replacing all occurences of the word "student" with "AMAZING student"
pretty_soup = pretty_soup.replace("student", "AMAZING student")



#Replacing the main picture with a picture of myself
pretty_soup = pretty_soup.replace("https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg", "https://scontent-ort2-1.xx.fbcdn.net/v/t1.0-9/10606355_10204523753278957_870926521847870674_n.jpg?oh=7885a71d4f89598c26e881cf8dc0b406&oe=5899602C")


#Replacing any local image with the image provided
pretty_soup = pretty_soup.replace("logo2.png", "logo.png")


#Making the html file reflect the changes on my website
f.write(pretty_soup)				


# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.




