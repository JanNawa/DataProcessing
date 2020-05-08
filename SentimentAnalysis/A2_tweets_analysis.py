# -*- coding: utf-8 -*-
"""
@author: Jan
"""
# import libraries
import csv
import re

# constants for polarity
POSITIVE = "positive"
NEGATIVE = "negative"
NEUTRAL = "neutral"

# create bag-of-words
def bag_of_words(str):
    word_count = dict()
    words = str.lower().split()

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

# get words from file and store in array
def get_words_from_file(file_loc):
    words = []
    for line in open(file_loc):
        line = line.strip()
        if not line.startswith(";"):
            words.append(line)
    return words

# compare keyword with the given list and add to words if in the give list
def compare_word(keyword, words, word_list):
    if keyword in word_list:
        if len(words) == 0:
            words = words + key
        else:
            words = words + "|" + keyword
    return words

# calculate the score
def calculate_score(positive, negative, bow_tweet):
    score = 0
    if len(positive) > 0:
        positives = positive.split("|")
        for p in positives:
            score = score + bow_tweet[p]
    if len(negative) > 0:      
        negatives = negative.split("|")
        for n in negatives:
            score = score - bow_tweet[n]
    return score

# set the polarity from the calculated score
def set_polarity(score):
    if score > 0:
        polarity = POSITIVE
    elif score == 0:
        polarity = NEUTRAL
    else:
        polarity = NEGATIVE
    return polarity

# read clean text from file
with open('tweet_text_1000.txt', 'r') as file:
    tweets = file.readlines()

# length of tweets
tweets_length = len(tweets)

# import positive and negative words from text file
positive_words = get_words_from_file(r"opinion-lexicon-english\positive-words.txt")
negative_words = get_words_from_file(r"opinion-lexicon-english\negative-words.txt")

# new array for finding
positive_match = []
negative_match = []
scores = []
polarities = []

# loop all the tweets
for tweet in tweets:
    # create bag-of-words for each tweet
    bow_tweet = bag_of_words(tweet)
    # collect positive and negative words from the tweet
    positive = ""
    negative = ""
    for key in bow_tweet.keys():
        # compare with positive words
        positive = compare_word(key, positive, positive_words)
        # compare with negative words
        negative = compare_word(key, negative, negative_words)
    positive_match.append(positive)
    negative_match.append(negative)
    # calculate score
    score = calculate_score(positive, negative, bow_tweet)
    scores.append(score)
    # assign polarity
    polarity = set_polarity(score)
    polarities.append(polarity)
  
# specify the header
headers = ["number", "tweets", "positive match", "negative match", "score", "polarity"]
# write to csv
with open('tweet_analysis_1000.csv', mode='w', newline='') as file:
    tweet_writer = csv.writer(file, escapechar=' ', quoting=csv.QUOTE_NONE)
    tweet_writer.writerow(headers)
    # loop all the collected data and write to row
    for x in range(tweets_length):
        clean_tweet = re.sub(r"\n", "", tweets[x])
        tweet_writer.writerow([x+1, clean_tweet, positive_match[x], negative_match[x], scores[x], polarities[x]])
