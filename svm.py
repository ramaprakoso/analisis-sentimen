import preprocessing
import pandas as pd
import csv
from sklearn import svm 
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm 
from sklearn.metrics import accuracy_score
from sklearn.learning_curve import learning_curve 


print "loading dictionary ... "

stop_words = [unicode(x.strip(), 'utf-8') for x in open('kamus/stopword.txt','r').read().split('\n')]
noise = [unicode(x.strip(), 'utf-8') for x in open('kamus/noise.txt','r').read().split('\n')]
stop_words.extend(noise)


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
                             min_df=0, preprocessor=preprocessing.preprocess,
                             stop_words=stop_words,tokenizer=preprocessing.get_fitur
                            )

X_test=vectorizer.fit_transform(docs_test).toarray()	
X_train=vectorizer.transform(docs_train).toarray()


print X_test
clf=svm.SVC(max_iter=1000)
clf.fit(X_train,y_train)

"""
title = 'Learning Curves (SVM, linear kernel, $\gamma=%.6f$)' %clf.best_estimator_.gamma
estimator = SVC(kernel='linear', gamma=clf.best_estimator_.gamma)
#plot_learning_curve(estimator, title, docs_train, y_train, cv=cv)
#plt.show()
#prediction=clf.predict(X_test)
"""
prediction=clf.predict(X_test)
#print prediction
#print 'accuracy : ',accuracy_score(y_test,prediction)                    
