import csv
import os
import re
import numpy as np 
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer


from nltk import word_tokenize
from nltk.stem import PorterStemmer
# import pattern.en
# from pattern.en import suggest
count_vect = CountVectorizer()
stopwords={'your', 'each', 'such', 're', 'both', 'couldn', 'doing', 'i', "don't", 'because', 'ours', 'how', 'd', 'we', 'those', 'doesn', "shouldn't", 'and', 'will', 'between', 'wouldn', 'shouldn', 'not', 'while', 'she', "won't", 'other', 'y', 'didn', 'me', 'into', 'was', 'he', 'most', 'under', 'aren', 'below', "hadn't", 'so', 'should', 'hasn', 'why', 'very', "you've", 'is', 'be', 'mightn', "aren't", 'during', 'my', 'as', 'been', 'll', 'were', 'hers', 'did', 'then', 'itself', "should've", 'now', 've', 'all', 'yours', 'over', "doesn't", 'her', 'own', 't', "wasn't", 'it', "weren't", 'where', 'am', 'm', 'by', 'wasn', 'against', 'out', 'weren', 'this', 'more', 'at', 'above', 'too', 'ain', 'for', "hasn't", "you're", 'here', 'can', 'with', 'when', 'a', 'after', 'before', 'down', "mightn't", 'ourselves', 'there', 'but', 'isn', "needn't", 'an', 'them', 'being', 'mustn', 'what', 'our', 'to', 'they', 'myself', "didn't", 'yourself', "you'll", 'haven', 'himself', 's', 'nor', 'off', "haven't", "wouldn't", 'the', 'only', 'herself', 'themselves', "she's", "it's", 'theirs', 'again', 'these', 'any', 'won', 'or', 'about', "isn't", 'yourselves', 'that', "you'd", 'once', 'whom', 'are', 'some', "shan't", 'few', 'their', 'having', "mustn't", 'through', 'in', 'shan', 'from', 'you', 'him', 'ma', 'o', 'does', 'just', 'hadn', 'who', 'if', 'until', 'no', "couldn't", 'which', 'on', 'of', 'up', 'same', 'do', 'further', 'needn', 'his', 'don', 'had', "that'll", 'than', 'have', 'has', 'its', 'A','a', '.', 'we', 'the', 'The', 'We', '``', 'review_body', 'review_date'}

def unique(list1): 
    x = np.array(list1)
    return np.unique(x)
  

#os.chdir(r'./CSV_Files')
reader = csv.reader(open('test.csv', encoding="utf8"),quotechar='|')
list = []
for line in reader:
    for field in line:
        tokens = word_tokenize(field.lower())
        list.append(tokens)

# print(list)
# print(len(list))

flat = []
for i in list:
  for j in i:
    flat.append(j)
print("After Tokenization of CSV file:")
print (flat)
print(len(flat))


# Tokenization using split()
# list = []
# with open('imdb1.csv', encoding="utf-8", mode ='r') as csvfile:  # this will close the file automatically.
#     reader = csv.reader(csvfile)
#     for row in reader:
#         # print(row)
#         j = str(row)
#         list.append(j.split(' '))
#
#     print(list)
#     print(len(list))


# stop_words = set(stopwords.words("english"))
# print(stop_words)
filtered_list = []
csv_columns = ['word','freq']

for w in flat:
    if w not in stopwords:
        filtered_list.append(w)
print("After removing StopWords:")
print(filtered_list)
print(len(filtered_list))

#Removing punctuation

words = [word for word in filtered_list if word.isalpha()]
print("After Removing Punctuation:")
print(words)
print(len(words))

#Stemming

ps = PorterStemmer()
stem_list = []
for w in words:
    stem_list.append(ps.stem(w))
print("After Stemming Process:")
#stem_list =(unique(stem_list))
stem_list_unique = unique(stem_list)
dict_tmp ={}
for j in stem_list_unique : 
	dict_tmp[j] = stem_list.count(j)
	print (j)
	print (stem_list.count(j))
print (dict_tmp)
print (len(stem_list))

#dict to csv
w = csv.writer(open("output.csv", "w"))
for key, val in dict_tmp.items():
    w.writerow([key, val])
#writer.writerow(data)
#X_train_counts = count_vect.fit_transform(stem_list)
#df = pd.DataFrame(X_train_counts,columns=["count"],index=stem_list)
#print(df)

# #Spell Correction
#
# def reduce_lengthening(text):
#     pattern = re.compile(r"(.)\1{2,}")
#     return pattern.sub(r"\1\1", text)
#
# spell_list = []
# for w in words:
#     w = reduce_lengthening(w)
#     correct_word = suggest(w)
#     spell_list.append(correct_word)
# print(spell_list)
# print(len(spell_list))
