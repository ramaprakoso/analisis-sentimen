import preprocessing
import csv
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.feature_extraction.text import TfidfVectorizer 

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
