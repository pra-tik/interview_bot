import csv
import os
import re
import numpy as np 
import pandas as pd
import sys
from sklearn.feature_extraction.text import CountVectorizer
from nltk import word_tokenize
from nltk.stem import PorterStemmer
# import pattern.en
# from pattern.en import suggest
count_vect = CountVectorizer()
stopwords={'your', 'each', 'such', 're', 'both', 'couldn', 'doing', 'i', "don't", 'because', 'ours', 'how', 'd', 'we', 'those', 'doesn', "shouldn't", 'and', 'will', 'between', 'wouldn', 'shouldn', 'not', 'while', 'she', "won't", 'other', 'y', 'didn', 'me', 'into', 'was', 'he', 'most', 'under', 'aren', 'below', "hadn't", 'so', 'should', 'hasn', 'why', 'very', "you've", 'is', 'be', 'mightn', "aren't", 'during', 'my', 'as', 'been', 'll', 'were', 'hers', 'did', 'then', 'itself', "should've", 'now', 've', 'all', 'yours', 'over', "doesn't", 'her', 'own', 't', "wasn't", 'it', "weren't", 'where', 'am', 'm', 'by', 'wasn', 'against', 'out', 'weren', 'this', 'more', 'at', 'above', 'too', 'ain', 'for', "hasn't", "you're", 'here', 'can', 'with', 'when', 'a', 'after', 'before', 'down', "mightn't", 'ourselves', 'there', 'but', 'isn', "needn't", 'an', 'them', 'being', 'mustn', 'what', 'our', 'to', 'they', 'myself', "didn't", 'yourself', "you'll", 'haven', 'himself', 's', 'nor', 'off', "haven't", "wouldn't", 'the', 'only', 'herself', 'themselves', "she's", "it's", 'theirs', 'again', 'these', 'any', 'won', 'or', 'about', "isn't", 'yourselves', 'that', "you'd", 'once', 'whom', 'are', 'some', "shan't", 'few', 'their', 'having', "mustn't", 'through', 'in', 'shan', 'from', 'you', 'him', 'ma', 'o', 'does', 'just', 'hadn', 'who', 'if', 'until', 'no', "couldn't", 'which', 'on', 'of', 'up', 'same', 'do', 'further', 'needn','want','whenev', 'his', 'don', 'had', "that'll", 'than', 'have', 'has', 'its', 'A','a', '.', 'we', 'the', 'The', 'We', '``', 'review_body', 'review_date'}
score = 0
read_csv = csv.reader(open('/home/pcadmin/Desktop/Bot/src/main/resources/static/p/output.csv', encoding="utf8"),quotechar='|')
dict_list = []
#for line in read_csv:
#	print(line)
#reader = """  A class is a blueprint for the object."""
#Sreader = "Whenever I want to create an object in java, the blueprint on basis of which I create the object is called a class. The class in Java consists of methods and attributes which define how the object will be like."
#reader = "Java class is the blueprint or the prototype being used while creating an object consisting of various attributes and methods." 
userInput = sys.argv[1]
reader = userInput.replace("+"," ")
print("READERV> " +str(reader))
#reader= "A class is a user defined blueprint or prototype from which objects are created.  It represents the set of properties or methods that are common to all objects of one type."
def unique(list1): 
    x = np.array(list1)
    return np.unique(x)
  

#os.chdir(r'./CSV_Files')
list = []
#for line in reader:
#for field in reader:
tokens = word_tokenize(reader.lower())
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

uniqueStr = ' '.join(stem_list_unique)

print (stem_list_unique)

total_Score=0
total_match=0
max_list = []
len_read_csv=0
print("uniq > " +(uniqueStr))
for i in read_csv:
		print("in if")
		if i[0] in uniqueStr:
				score = score+int(i[1])
				total_match = total_match + 1
		total_Score = total_Score +int(i[1])
		max_list.append(int(i[1]))
		len_read_csv =len_read_csv+1
print("len_read_csv >> " +str(len_read_csv))
print(max_list)
max_list.sort(reverse = True)
print(max_list)
max_list = max_list[:len(stem_list_unique)]
print(max_list)		
print(score)
print(total_match)

init_var = (score*total_match)/(total_Score*len(stem_list_unique))
print(init_var)

#score,len(stem_list_unique), total_Score,total_match
print(total_Score)
finalVar =float( sum(max_list)/total_Score)
print(finalVar)
temp_Cal= len(stem_list_unique)/len_read_csv
print("len_temp cal >> " +str(temp_Cal))
result = temp_Cal*(init_var/finalVar)*100

print(result)

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
