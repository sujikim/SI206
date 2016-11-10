# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

import tweepy 
import requests

# Unique code from Twitter
access_token = "719012456849391618-ij1fpXyXaVgj8Q1fSCf6qJdVh0P9F1p"
access_token_secret = "dL6f1C79iKxihKRethnF95Qd1a7mxlyY30xKQvbquuV6C"
consumer_key = "5CZBJ3KoczmIavmP5kYXCnhLO"
consumer_secret = "XcAwYn51YR9RSGb816JCNjVovU1eExP2kvZs2cINSHTaG32D54"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
my_img = "samoyed-puppy-01.jpg"

api.update_with_media(my_img, status = "#UMSI-206 should bring in Samoyed puppies after the #Proj3 deadline!")
