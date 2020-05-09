# Data Processing

Data Processing for Semantic and Sentiment Analysis

## Files and External Data

### [SemanticAnalysis](SemanticAnalysis)

**Overview**

The program extracts data from news API and stores data in document repository.
Then, the program evaluate TF-IDF to evaluate the documents in document repository.

**Source Code**

1. [B1_extract_news.py](SemanticAnalysis/B1_extract_news.py)

The program retrieves the news articles from news API using the specified keywords.
Then, the program extract only “title”, “description”, and “content” from each news article.
Next, write the retrieved data to text file and store in “documents” folder.

The sample of documents are in [documents](SemanticAnalysis/documents)

2. [B2_news_TF-IDF.py](SemanticAnalysis/B2_news_TF-IDF.py)

The program uses Term frequency-inverse document frequency (TF-IDF) to evaluate the relevant of keyword in a document in document repository. 
TF-IDF is done by measuring 2 things which are document frequency and term frequency.

The source code divided into 3 sections:\
* **Part A** : Document Frequency\
Calculate the value of document frequency that related to the keywords.\
The [output of document frequency](SemanticAnalysis/output/A_document_frequency.csv) is saved in CSV format.\
* **Part B** : Term Frequency\
Calculate the value of term frequency that related to the keywords.\
The [output of term frequency](SemanticAnalysis/output/B_term_frequency.csv) is saved in CSV format.\
* **Part C** : Print the news article with the highest relative frequency on the console

The sample of output are in [output](SementicAnalysis/output).

### [SentimentAnalysis](SentimentAnalysis)

**Overview**
XXX

**Source Code**

1. [A1_tweets_clean.py](SentimentAnalysis/A1_tweets_clean.py)
The program select 1,000 tweets’ text from REST key in [twitter_A3_data.json](SentimentAnalysis/twitter_A3_data.json). 
Then, cleaning data by removing RT, special characters, and multiple spaces from the text.
The program writes data to [text file](SentimentAnalysis/tweet_text_1000.txt).

2. [A2_tweets_analysis.py](SentimentAnalysis/A2_tweets_analysis.py)
The program creates bag-of-words for each tweet. Then, compare each bag-of-word with a list of [positive words](SentimentAnalysis/opinion-lexicon-english/positive-words.txt) and [negative words](SentimentAnalysis/opinion-lexicon-english/negative-words.txt).
This method is sentiment analysis in lexicon-based approach by creating dictionary and using key-value pair to count the number of occurrences of the word in the sentence.

Then, the program calculates the score and decides whether the polarity is positive, neutral, or negative. 
If the word is in the list of positive words, the word will multiply by 1 with the number of occurrences of that word. 
However, if the word is in the list of negative words, the word will multiply by -1 with the number of occurrences of that word. 
The number from positive and negative is added and result in score. 
If the score is more than 0, it is positive. 
If the score is equal to 0, it is neutral. 
If the score is less than 0, it is negative.

The program writes data and analysis in [CSV file](SentimentAnalysis/tweet_analysis_1000.csv).

3. [A3_tweets_analysis_word_count.py](SentimentAnalysis/A3_tweets_analysis_word_count.py)
The program counts the word frequency of positive and negative words.
Then, the program writes the positive words with the number of word count in [CSV file](SentimentAnalysis/positive_count.csv).
Next, the program writes the negative words with the number of word count in [CSV file](SentimentAnalysis/negative_count.csv).

### Dependencies

Python libraries
* requests
* pandas
* json
* csv
* re
* os
* math

### Acknowledgments

* http://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html
