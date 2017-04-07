import preprocessing 
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import csv
import collections
import pickle 
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

train_df_raw = pd.read_csv('dataset_final/training90.csv',sep=';',names=['tweets','label'],header=None)
test_df_raw = pd.read_csv('dataset_final/testing10.csv',sep=';',names=['tweets','label'],header=None)
train_df_raw = train_df_raw[train_df_raw['tweets'].notnull()]
test_df_raw = test_df_raw[test_df_raw['tweets'].notnull()]

#ekstrak make training and testing 
X_train=train_df_raw['tweets'].tolist()

X_test=test_df_raw['tweets'].tolist()
y_train=[x if x==0 else 1 for x in train_df_raw['label'].tolist()]

#tanpa cross validation , manual label 
#y_test=[x if x=='1' else '0' for x in test_df_raw['label'].tolist()]

vectorizer = TfidfVectorizer(max_df=1.0, max_features=2000,
                             min_df=0, preprocessor=preprocessing.preprocess,
                             stop_words=stop_words,tokenizer=preprocessing.get_fitur
                            )

X_train=vectorizer.fit_transform(X_train).toarray()
X_test=vectorizer.transform(X_test).toarray()

#fitur 
feature_names=vectorizer.get_feature_names()
# idf=vectorizer.idf_
#tampilkan fitur 
#print feature_names
#jumlah fitur 
print len(feature_names)
#menampilkan fitur yang sudah di tf-idf 
# print dict(zip(vectorizer.get_feature_names(), idf))
# print len(vectorizer.get_feature_names(),idf)
print "Load classifier ... "
#setting multinomial sebagai entropy 
MaxEnt=linear_model.MaximumEntropy(max_iter=1000,multi_class='multinomial',solver='lbfgs')
#print MaxEnt
MaxEnt.fit(X_train,y_train)



#saving training
#filesave='save_train/maxentfold5.sav'
#pickle.dump(MaxEnt,open(filesave,'wb'))
weighted_prediction=MaxEnt.predict(X_test)

print "Count Accuracy ... "
skf=StratifiedKFold(n_splits=5,random_state=0)
scores=cross_val_score(MaxEnt,X_train,y_train,cv=skf)
precision_score=cross_val_score(MaxEnt,X_train,y_train,cv=skf,scoring='precision')
recall_score=cross_val_score(MaxEnt, X_train,y_train, cv=skf, scoring ='recall')


print "Recall :%0.2f"%recall_score.mean()
print "Precision :%0.2f"%precision_score.mean()
print "Accuracy :%0.2f" % scores.mean()

#print collections.Counter(weighted_prediction)	 
labels, values = zip(*Counter(weighted_prediction).items())

SentimenPositif=values[1]
SentimenNegatif=values[0]
#SentimenPositif.append(values[1])
#SentimenNegatif.append(values[0])


ind=np.arange(1)
width=0.8
#fig = plt.figure()
ax = plt.subplot(111)


yvals = SentimenPositif
rects1 = ax.bar(ind, yvals, width, color='blue')
zvals = SentimenNegatif
rects2 = ax.bar(ind+width, zvals, width, color='red')
ax.set_ylabel("Frequency")

ax.set_xticks(ind+width)
ax.set_xticklabels(("Ahok","Agus","Anies"))
ax.legend((rects1[0], rects2[0]), ('Positif', 'Negatif'))

for rect in rects1:
	h = rect.get_height()
	ax.text(rect.get_x()+rect.get_width()/2,1*h, '%d'%int(h),ha='center',va='bottom') 

for rect in rects2:
	h = rect.get_height()
	ax.text(rect.get_x()+rect.get_width()/2,1*h, '%d'%int(h),ha='center',va='bottom') 

#plt.axis([0,10, 0,300])
plt.title("Grafik Analisis Sentimen")
plt.show()

"""
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
plt.axis([0,10, 0,500])
plt.legend(('Negatif', 'Negatif'))
plt.show()
"""

#print 'Accuracy:', accuracy_score(y_test, weighted_prediction)
"""
print 'F1 score:', f1_score(y_test, weighted_prediction,average='weighted')
print 'Recall:', recall_score(y_test, weighted_prediction, average='weighted')
"""
#print 'Precision:', precision_score(y_test, weighted_prediction,
 #                               average='weighted')
