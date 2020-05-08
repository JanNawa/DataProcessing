# -*- coding: utf-8 -*-
"""
@author: Jan
"""
# import libraries
import pandas as pd
import csv

# variables
POSITIVE = "positive  match"
NEGATIVE = "negative  match"
delimiter = "|"

# create string from series
def create_string(series, delimiter):
    # drop columnn that in nan
    series.dropna()
    series_str = ""

    # use for add the first word in string
    flag = True
    

    for item, words in series.items():
        words_str = str(words)
        if words_str == "nan":
            continue
        if flag:
            series_str = words_str
            flag = False
        series_str = series_str + delimiter + words_str
    return series_str
    
# create bag-of-words
def bag_of_words(str):
    word_count = dict()
    words = str.split(delimiter)

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

# write dictionary to csv file
def write_csv(filename, dictionary):
    with open(filename, mode='w', newline='') as f:
        w = csv.writer(f)
        w.writerows(dictionary.items())

# count word frequency and save to csv
def count_word_to_csv(series, csv_filename):
    series_str = create_string(series, delimiter)
    word_count = bag_of_words(series_str)
    write_csv(csv_filename, word_count)


# import dataset
words = pd.read_csv(r'tweet_analysis_1000.csv')
# column that want to count word frequency
positives = words[POSITIVE]
negatives = words[NEGATIVE]
count_word_to_csv(positives, "positive_count.csv")
count_word_to_csv(negatives, "negative_count.csv")