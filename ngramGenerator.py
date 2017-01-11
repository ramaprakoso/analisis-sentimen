# N-gram generator based on nltk module
# K-most frequent words in a class od tweets
import nltk
import operator # for sorting dictionnares

# getting word frequencies from training data for a given class

def getTweetWords(tweet):
    all_words = []
    sTweet=tweet.split()
    return sTweet

def get_word_features(wordlist): # from a list of words returns a dictionnary with word, freq as key, value
    wordlist = nltk.FreqDist(wordlist)
    result=[]
    for k in wordlist.keys():
        result.append([k,wordlist[k]])
    return result

def ngramText(filename): # generate vector of ngrams in text file
    textWords=[]
    f=open(filename,"r")
    line=f.readline()
    while line:
        textWords.extend(getTweetWords(line))
        line=f.readline()
    f.close()
    return textWords

def sortList(x):
    return list(reversed(sorted(x, key=operator.itemgetter(1))))

def mostFreqList(filename): # extract k most frequent words from the sorted list
    d=get_word_features(ngramText(filename))
    l=sortList(d)
    m=[w[0] for w in l]
    return m
    
    
#filename="dataset/pos.csv"
#print ngramText(filename)
#print mostFreqList(filename)
"""
import numpy as np 
from numpy import reshape,arange

from sklearn.cross_validation import train_test_split
from sklearn import preprocessing
from sklearn import datasets
import matplotlib.pyplot as plt
iris=datasets.load_iris()
X_iris,y_iris=iris.data,iris.target
#Get dataset with only the first two attributes 
X,y=X_iris[:,:2],y_iris
#split the dataset into a training and a testing set 
#Test set will be 25% taken randomly 
X_train, X_test, y_train, y_test = train_test_split(X, y,
test_size=0.25, random_state=33)
# Standardize the features
scaler = preprocessing.StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

colors = ['red', 'greenyellow', 'blue']
for i in xrange(len(colors)):
	xs = X_train[:, 0][y_train == i]
	ys = X_train[:, 1][y_train == i]
plt.scatter(xs, ys, c=colors[i])
plt.legend(iris.target_names)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
"""
