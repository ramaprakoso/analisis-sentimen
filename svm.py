import preprocessing 
import pandas as pd
from sklearn import svm 
from sklearn.metrics import accuracy_score

print "loading feature ..."
fp=open('dataset/train_fitur.csv','r')
line=fp.read()
pre=preprocessing.preprocess(line)
fitur=preprocessing.get_fitur(pre)
print fitur 
#print get_fitur 
#train_df = pandas.read_csv('train.csv',sep=',',dtype={'label':int, 'tweet':str})







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
