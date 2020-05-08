# -*- coding: utf-8 -*-
"""
@author: Jan
"""

# Importing the libraries
import json
import re

# Import json
with open("twitter_A3_data.json", "r") as read_file:
    tweets = json.load(read_file)

# clean text
def cleanTweet(text):
    # replace RT with ""
    text = re.sub("RT","", text)    
    # replace special character with space
    text = re.sub(r"[^0-9a-zA-Z-]"," ", text)
    # replace multiple spaces with single space
    text = re.sub(r"\s+"," ", text)
    return text.strip()

max_record = 1000
tweet_text = ""
# store 1,000 tweets to "tweet_text" variable
for x in range(max_record):
    # each line represents 1 tweet
    text_only = cleanTweet(tweets["REST"][x]["text"])
    if (x == max_record-1):
        tweet_text = tweet_text + text_only
    else:
        tweet_text = tweet_text + text_only + "\n"

# write "tweet_text" to text file
text_file = open("tweet_text_1000.txt", "w")
text_file.write(tweet_text)
text_file.close()