import preprocessing
import csv
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.feature_extraction.text import TfidfVectorizer 

from collections import defaultdict
import csv 

docs=defaultdict(list)
with open("tweet3000id.csv",'r') as sentences_file : 
	reader=csv.reader(sentences_file,delimiter=';')
	reader.next()
	
	for row in reader: 
		docs[row[0]].append(row[1])
	
for id_tweets,tweets in docs.iteritems() : 
	docs[id_tweets]="".join(tweets)
corpus=[]
#append tweets to corpus 
for id,tweets in sorted(docs.iteritems(), key=lambda t: int(t[0])):
	corpus.append(tweets)

fp = open('tweet3000.csv', 'r')
line = fp.read()
#preprocessing tweets raw
pre=preprocessing.preprocess(line)
#get feature 
f=preprocessing.get_fitur(pre)
#remove redundant words  
fitur=list(set(f))

vectorizer = TfidfVectorizer(analyzer='word', ngram_range=(1,1), min_df = 0, vocabulary=fitur)
X = vectorizer.fit_transform(corpus)
idf = vectorizer._tfidf.idf_
print dict(zip(vectorizer.get_feature_names(), idf))

"""
#open file 
fp = open('tweet3000.csv', 'r')
line = fp.read()
#preprocessing
pre=preprocessing.preprocess(line)
#ambil fitur
f=preprocessing.get_fitur(pre)
#hapus redudansi fitur 
fitur=list(set(f))
cv=CountVectorizer(vocabulary=fitur)
X=cv.fit_transform(pre)

print X.toarray()
"""
