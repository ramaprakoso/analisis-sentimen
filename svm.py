import preprocessing 
import pandas as pd
import csv
from sklearn import svm 
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm 
from sklearn.metrics import accuracy_score

print "loading feature ..."
fp=open('dataset/train_fitur.csv','r')
line=fp.read()
pre=preprocessing.preprocess(line)
fitur=preprocessing.get_fitur(pre)

train_df_raw = pd.read_csv('dataset/train.csv',sep=';',names=['tweets','label'],header=None)
test_df_raw = pd.read_csv('dataset/testing.csv',sep=';',names=['tweets','label'],header=None)
train_df_raw = train_df_raw[train_df_raw['tweets'].notnull()]
test_df_raw = test_df_raw[test_df_raw['tweets'].notnull()]

#ekstrak make training and testing 
docs_train=train_df_raw['tweets'].tolist()
docs_test=test_df_raw['tweets'].tolist()
y_train=[x if x=='positif' else 'negatif' for x in train_df_raw['label'].tolist()]
y_test=[x if x=='positif' else 'negatif' for x in test_df_raw['label'].tolist()]

vectorizer = TfidfVectorizer(max_df=1.0, max_features=10000,
                             min_df=0, vocabulary=fitur)
vectorizer.fit(docs_test+docs_train)
X_train=vectorizer.transform(docs_train)
X_test=vectorizer.transform(docs_test)

clf=svm.SVC(max_iter=1000)
clf.fit(X_train,y_train)

prediction=clf.predict(X_test)
print 'accuracy : ',accuracy_score(y_test,prediction)                    
"""
KERNEL_FUNCTION="linear"
C_PARAMETER=0.6

print "Building Bag Of Words"
positif=ngramGenerator.mostFreqList('dataset/pos.csv')
negatif=ngramGenerator.mostFreqList('dataset/neg.csv')

for w in positif: 
	if w in negatif: 
		positif.remove(w)
for w in negatif: 
	if w in positif: 
		negatif.remove(w)
#equalize unigram size 

m=min(len(positif),len(negatif))
"""
