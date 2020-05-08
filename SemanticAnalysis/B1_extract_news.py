# -*- coding: utf-8 -*-
"""
@author: Jan
"""
# import libraries
import requests as r
import json as js
import os

NEW_LINE = "\n"
DIRECTORY_SEPARATOR = "\\"

# get news from news api and return list of data
def get_news_from_api(apiKey, keywords):
    data = []
    # go through all the keywords
    for keyword in keywords:
        # for search the keyword in news api
        searchUrl = "http://newsapi.org/v2/everything?q=" + keyword + "&apiKey=" + apiKey + "&pageSize=100"
        # connect to url and get the result
        result = r.get(searchUrl)
        # read the output from the result
        data1 = result.text
        # remove escape characters
        data1 = data1.replace("\\r\\n", "")
        # convert the string to JSON
        parsedJS = js.loads(data1)
        # get the article part
        articles = parsedJS["articles"]
        data.append(articles)
    return data

# extract specific fields and save as text files
def extract_news_to_text_file(directory, data):
    # use to loop through the list of data
    data_length = len(data)
    # count the number of documents, this will be used in file name
    count = 1
    # loop through all the items in list of data
    for x in range(data_length):
        nested_length = len(data[x])
        for y in range(nested_length):
            # extract specific fields
            title = data[x][y]["title"]
            desc = data[x][y]["description"]
            content = data[x][y]["content"]
            
            if not os.path.exists(directory):
                os.makedirs(directory)  
            
            # write data to text file    
            with open(directory + DIRECTORY_SEPARATOR + "news_" + str(count) + ".txt", "w", encoding="utf-8") as text_file:
                if title:
                    text_file.write(title + NEW_LINE) 
                if desc:
                    text_file.write(desc + NEW_LINE) 
                if content:
                    text_file.write(content + NEW_LINE)        
            # increase count for next file
            count = count + 1

# keyword that will be used for search in news api
keywords = ["Canada", "university", "Dalhousie University", "Halifax", "business"]
apiKey = "xxx"
# run the function
data = get_news_from_api(apiKey, keywords)
extract_news_to_text_file("documents", data)
