# -*- coding: utf-8 -*-
"""
@author: Jan Chayopathum
"""
# import libraries
import os
import math
import csv

# define constant
NEW_LINE = "\n"
DIRECTORY_SEPARATOR = "\\"

# write data to csv
def write_to_csv(directory, filename, headers, rows):
    if not os.path.exists(directory):
        os.makedirs(directory)
    # write data to text file    
    with open(directory + DIRECTORY_SEPARATOR + filename, mode='w', newline='') as csv_file:        
        csv_writer = csv.writer(csv_file)
        # write headers
        for header in headers:
            csv_writer.writerow(header)
        # loop all the collected data and write to row
        for row in rows:
            csv_writer.writerow(row)

# create rows of data
def create_rows(arg1, arg2, arg3, arg4):
    rows = []
    arg_length = len(arg1)
    for x in range(arg_length):
        rows.append([arg1[x], arg2[x], arg3[x], arg4[x]])
    return rows

# =============================================================================
# A - Document Frequency (df)
# =============================================================================
def get_total_documents(folder_name):
    dir_list = os.listdir(folder_name) # specify the directory that want to count the files
    return len(dir_list)

def find_df(keywords, total_documents):
    df = []
    for keyword in keywords:
        count_keyword = 0
        for x in range(total_documents):
            with open("documents\\news_" + str(x+1) + ".txt", "r", encoding="utf-8") as f:
                if keyword in f.read():
                    count_keyword = count_keyword + 1
        df.append(count_keyword)
    return df

def find_ndf(df, total_documents):
    ndf = []
    for number in df:
        ndf.append(str(total_documents) + "/" + str(number))
    return ndf

def find_log_ndf(ndf, base):
    log_ndf = []
    for number in ndf:
        log_ndf.append(round(math.log(eval(number), base), 2))
    return log_ndf
    
# create heading
csv_title = "Total Documents"
total_documents = get_total_documents("documents")
# first header
csv_heading = [csv_title, total_documents]
# second header
csv_columns = ["Search Query", "Document containing term (df)", "Total Documents (N) / number of documents term appeared (df)", "Log 10 (N/df)"]
headers = [csv_heading, csv_columns]

# create rows of data   
# keyword that will be used for search in documents
keywords = ["Canada", "university", "Dalhousie University", "Halifax", "business"]
df = find_df(keywords, total_documents)
ndf = find_ndf(df, total_documents)
log_ndf = find_log_ndf(ndf, 10)
rows = create_rows(keywords, df, ndf, log_ndf)
# write to csv
write_to_csv("output", "A_document_frequency.csv", headers, rows)

# =============================================================================
# B - Term Frequency (tf)
# =============================================================================

# find the document that have the term
def find_doc_names(term, total_documents):
    doc_names = []
    for x in range(total_documents):
        with open("documents\\news_" + str(x+1) + ".txt", "r", encoding="utf-8") as f:
            if term in f.read():
                doc_names.append("news_" + str(x+1) + ".txt")
    return doc_names

# find total of words in the documents
def find_total_words(term, doc_names):
    total_words = []
    for doc_name in doc_names:
        with open("documents\\" + doc_name, "rt", encoding="utf-8") as f:
            text = f.read()
            total_word = len(text.split())
            total_words.append(total_word)
    return total_words

# find frequency of term in documents
def find_frequencies(term, doc_names):
    frequencies = []
    for doc_name in doc_names:
        with open("documents\\" + doc_name, "rt", encoding="utf-8") as f:
            text = f.read()
            all_words = text.split()
            count = 0
            for word in all_words:
                if term in word:
                    count = count + 1
            frequencies.append(count)
    return frequencies

# find term frequency values
def find_df(frequencies, total_words):
    tf = []
    length = len(frequencies)
    for x in range(length):
        tf.append(round(frequencies[x]/total_words[x], 2))
    return tf

# create heading
csv_term = "Term"
term = "Canada"
# first header
csv_heading = [csv_term, term]

index_term = keywords.index(term)
doc_frequency_term = df[index_term]
# second header
csv_columns = [term + " appeared in " + str(doc_frequency_term) + " documents", "Total Words (m)", "Frequency (f)", "Term Frequency (f/m)"]
headers = [csv_heading, csv_columns]

# create rows of data
doc_names = find_doc_names(term, total_documents)
total_words = find_total_words(term, doc_names)
frequencies = find_frequencies(term, doc_names)
tf = find_df(frequencies, total_words)
rows = create_rows(doc_names, total_words, frequencies, tf)

# write to csv
write_to_csv("output", "B_term_frequency.csv", headers, rows)

# =============================================================================
# C - print the news article with the highest relative frequency
# =============================================================================

# print the document to the console
def print_doc(directory, names):
    for name in names:
        print("==============================================")
        print(name)
        print("==============================================")
        with open(directory + DIRECTORY_SEPARATOR + name, "r", encoding="utf-8") as f:
            print(f.read())
        
# find the maximum term frequency (f/m) of "canada"
max_fm = max(tf)
# find all the indices that has maximum term frequency
doc_indices = [i for i, x in enumerate(tf) if x == max_fm]
# collect all filenames in the list
names = []
for x in doc_indices:
    names.append(doc_names[x])
# print news article that has highest term frequency on the console
print_doc("documents", names)    