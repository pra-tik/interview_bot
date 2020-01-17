import pandas as pd
df = pd.read_csv("imdb1.csv")
reviews = df.review_body #you can also use df['column_name']
labels = df.rating

for i in labels:
    if labels[i]>=30:
        file1 = open("positive.txt", "a")  # append mode
        file1.write(reviews[i]+"\n")
        file1.close()

for i in labels:
    if labels[i]<30:
        file1 = open("negative.txt", "a")  # append mode
        file1.write(reviews[i] + "\n")
        file1.close()