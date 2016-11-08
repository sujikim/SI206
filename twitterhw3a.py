# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

import tweepy 

from TwitterAPI import requests

# Unique code from Twitter
access_token = "719012456849391618-ij1fpXyXaVgj8Q1fSCf6qJdVh0P9F1p"
access_token_secret = "dL6f1C79iKxihKRethnF95Qd1a7mxlyY30xKQvbquuV6C"
consumer_key = "5CZBJ3KoczmIavmP5kYXCnhLO"
consumer_secret = "XcAwYn51YR9RSGb816JCNjVovU1eExP2kvZs2cINSHTaG32D54"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

file = open('samoyed-dog-hereditary-health-and-health-testing-55015c6bb5bda.jpg', 'rb')
data = file.read()
r = api.request('statuses/update_with_media', {'status':'my favorite dog!!'}, {'media[]':data})
print(r.status_code)



print("""No output necessary although you 
	can print out a success/failure message if you want to.""")

