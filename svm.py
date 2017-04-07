import preprocessing 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import pickle 
from sklearn import svm 
from collections import Counter
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm 
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn import metrics


#ambil kamus stopword dalam class preprocessing
print "loading dictionary ... "
stop_words = [unicode(x.strip(), 'utf-8') for x in open('kamus/stopword.txt','r').read().split('\n')]
noise = [unicode(x.strip(), 'utf-8') for x in open('kamus/noise.txt','r').read().split('\n')]
stop_words.extend(noise)
print "Complate"
print "\n"
print "\n"

#persiapan data testing dan training
print "Preparing data ..."
train_df_raw = pd.read_csv('dataset_final/training90.csv',sep=';',names=['tweets','label'],header=None)
test_df_raw = pd.read_csv('dataset_final/testing10.csv',sep=';',names=['tweets','label'],header=None)
train_df_raw = train_df_raw[train_df_raw['tweets'].notnull()]
test_df_raw = test_df_raw[test_df_raw['tweets'].notnull()]

print "Complate"
print "\n"
print "\n"

#ambil data training
X_train=train_df_raw['tweets'].tolist()

#sample preprocessing 
# for tweet in X_train: 
# 	tweets=tweet
# 	pre=preprocessing.preprocess(tweets)
# 	fitur=preprocessing.get_fitur_all(pre)
# 	print fitur

#ambil data testing
X_test=test_df_raw['tweets'].tolist()
# print X_train
# print X_test

#ambil label 
y_train=[x if x==1 else 0 for x in train_df_raw['label'].tolist()]

#tanpa cross validation , manual label (unseen data)
#y_test=[x if x=='positif' else 'negatif' for x in test_df_raw['label'].tolist()]
print "Pipelining process ..."

#proses pembobotan tf-idf 
vectorizer = TfidfVectorizer(max_df=1.0, max_features=2000,
                             min_df=0, preprocessor=preprocessing.preprocess,
                             stop_words=stop_words,tokenizer=preprocessing.get_fitur
                            )
# vectorizer = TfidfVectorizer(max_df=1.0, max_features=10000,
#                              min_df=0, preprocessor=preprocessing.preprocess,
#                              stop_words=stop_words,vocabulary=preprocessing.get_fitur
#                             )
#fitur setalah dilakukan pembobotan 
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


#Hitung jumlah fitur 
# print len(X_train)
# print len(X_test)

print "Complate"
print "\n"
print "classfication ..."

#klasifikasi support vector machine 
clf=svm.SVC(kernel='linear',gamma=1)
clf.fit(X_train,y_train)

#simpan data training 

#filesave='save_train/svmlinear9010.sav'
#pickle.dump(clf,open(filesave,'wb'))
#clf = pickle.load(open(filesave, 'rb'))
print "Complate"
print "\n"
#train model 
skf=StratifiedKFold(n_splits=5,random_state=0)
scores=cross_val_score(clf,X_train,y_train,cv=skf)
precision_score=cross_val_score(clf,X_train,y_train,cv=skf,scoring='precision')
recall_score=cross_val_score(clf, X_train,y_train, cv=skf, scoring ='recall')

#scoring                                                                                                                                                                                                                                             b                                                                                                                                                                                                                  
print "Result ..."
print "Recall :%0.2f"%recall_score.mean()
print "Precision :%0.2f"%precision_score.mean()
print "Accuracy :%0.2f"%scores.mean()

#prosentase grafik
weighted_prediction=clf.predict(X_test)
#print len(weighted_prediction)

"""
c=Counter(weighted_prediction)
plt.bar(c.keys(),c.values())
"""

#ambil nilai prediksi dari variabel weighted_prediction 
labels, values = zip(*Counter(weighted_prediction).items())
indexes=np.arange(len(labels))
width=0.9
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

#membuat grafik batang 
yvals = SentimenPositif
rects1 = ax.bar(ind, yvals, width, color='blue')
zvals = SentimenNegatif
rects2 = ax.bar(ind+width, zvals, width, color='red')
ax.set_ylabel("Frequency")

ax.set_xticks(ind+width)
ax.set_xticklabels(("Result","a","b"))
ax.legend((rects1[0], rects2[0]), ('Positif', 'Negatif'))

for rect in rects1:
	h = rect.get_height()
	ax.text(rect.get_x()+rect.get_width()/2,0.99*h, '%d'%int(h),ha='center',va='bottom') 

for rect in rects2:
	h = rect.get_height()
	ax.text(rect.get_x()+rect.get_width()/2,0.99*h, '%d'%int(h),ha='center',va='bottom') 

#plt.axis([0,10, 0,300])
plt.title("Grafik Analisis Sentimen")
plt.show()

"""
plt.bar(indexes, values, width,color=['red', 'blue'])
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
"""

#print collections.Counter(weighted_prediction)	 

"""
print 'Recall:', recall_score(y_test, weighted_prediction,
                              average='weighted')
print 'Precision:', precision_score(y_test, weighted_prediction,
                             average='weighted')
"""
