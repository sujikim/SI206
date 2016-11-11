# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

import tweepy
from textblob import TextBlob
import sys 

# Unique code from Twitter


# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

#Now we can Create Tweets, Delete Tweets, and Find Twitter Users
api = tweepy.API(auth)
print ("------------------------------------------------------------------")
search_topic = input("Please enter a Twitter search topic of your choice: ")
print ("------------------------------------------------------------------")
public_tweets = api.search(search_topic)
total_subjectivity = 0
total_polarity = 0
t_sub = 0
t_pol = 0

print ("TWEETS ABOUT", search_topic.upper(), ":")

#Creating a for loop to count the total number of tweets and get its respective polarity and subjectivity scores
for tweet in public_tweets:
	print (tweet.text)
	analysis = TextBlob(tweet.text)
	t_sub += analysis.sentiment.subjectivity
	t_pol += analysis.sentiment.polarity
	total_subjectivity += 1
	total_polarity += 1

print ("*******************************************")
#Calculating and printing out the average subjectivity and polarity scores of the collected tweets
avg_subjectivity = t_sub/total_subjectivity
avg_polarity = t_pol/total_polarity
print("Average subjectivity is", avg_subjectivity)
print("Average polarity is", avg_polarity)
print ("*******************************************")

