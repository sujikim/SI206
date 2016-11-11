# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

import tweepy 
import requests

# Unique code from Twitter


auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

#Setting a variable to the picture I want to tweet
api = tweepy.API(auth)
my_img = "samoyed-puppy-01.jpg"

#Uploading my image with a message to my Twitter account
api.update_with_media(my_img, status = "#UMSI-206 should bring in Samoyed puppies after the #Proj3 deadline!")
