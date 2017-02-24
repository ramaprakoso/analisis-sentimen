import preprocessing 
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import csv
import collections
from collections import Counter
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn import svm 
from sklearn import linear_model 
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm 
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score


print "loading dictionary ... "

stop_words = [unicode(x.strip(), 'utf-8') for x in open('kamus/stopword.txt','r').read().split('\n')]
noise = [unicode(x.strip(), 'utf-8') for x in open('kamus/noise.txt','r').read().split('\n')]
stop_words.extend(noise)

train_df_raw = pd.read_csv('dataset/train.csv',sep=';',names=['tweets','label'],header=None)
test_df_raw = pd.read_csv('dataset/testing.csv',sep=';',names=['tweets','label'],header=None)
train_df_raw = train_df_raw[train_df_raw['tweets'].notnull()]
test_df_raw = test_df_raw[test_df_raw['tweets'].notnull()]

#ekstrak make training and testing 
X_train=train_df_raw['tweets'].tolist()
X_test=test_df_raw['tweets'].tolist()
y_train=[x if x==1 else 0 for x in train_df_raw['label'].tolist()]
#y_test=[x if x=='1' else '0' for x in test_df_raw['label'].tolist()]

vectorizer = TfidfVectorizer(max_df=1.0, max_features=10000,
                             min_df=0, preprocessor=preprocessing.preprocess,
                             stop_words=stop_words,tokenizer=preprocessing.get_fitur
                            )

X_train=vectorizer.fit_transform(X_train)
X_test=vectorizer.transform(X_test)


print "Load classifier ... "
MaxEnt=linear_model.MaximumEntropy()
MaxEnt.fit(X_train,y_train)
weighted_prediction=MaxEnt.predict(X_test)

print "Count Accuracy ... "
skf=StratifiedKFold(n_splits=2,random_state=0)
scores=cross_val_score(MaxEnt,X_train,y_train,cv=skf)
precision_score=cross_val_score(MaxEnt,X_train,y_train,cv=skf,scoring='precision')
recall_score=cross_val_score(MaxEnt, X_train,y_train, cv=skf, scoring ='recall')

print "Precision :%0.2f"%precision_score.mean()
print "Recall :%0.2f"%recall_score.mean()
print "Accuracy :%0.2f" % scores.mean()

#print collections.Counter(weighted_prediction)	 
labels, values = zip(*Counter(weighted_prediction).items())

indexes=np.arange(len(labels))
width=0.9

plt.bar(indexes, values, width,color=['red','blue'])
labels=list(labels)
labels[0]='negatif'
labels[1]='positif'
labels=tuple(labels)
plt.title("Hasil Sentimen Analisis")
plt.xticks(indexes + width * 0.5, labels)
plt.ylabel('Scores')
plt.xlabel('Label')
plt.plot(kind='bar')
plt.show()

#print 'Accuracy:', accuracy_score(y_test, weighted_prediction)
"""
print 'F1 score:', f1_score(y_test, weighted_prediction,average='weighted')
print 'Recall:', recall_score(y_test, weighted_prediction, average='weighted')
"""
#print 'Precision:', precision_score(y_test, weighted_prediction,
 #                               average='weighted')
