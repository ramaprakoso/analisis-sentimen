import preprocessing
import csv
import svm 
from svmutil import *

def getSVMFeatureLabel(tweets,featureList): 
	sorting_fitur=sorted(featureList)
	map={}
	featureVector=[]
	labels=[]
	for t in tweets: 
		label=0
		map={}
		for w in sorting_fitur:
			map[w]=0
		tweet_words=t[0]
		sentimen=t[1]
		for word in tweet_words.split(): 
			word=preprocessing.hapus_katadouble(word)
			if word in map: 
				map[word]=1
		#end loops
		values=map.values()
		featureVector.append(values)
		if(sentimen=='positif'):
			label=0
		elif(sentimen=='negatif'): 
			label=1
		elif(sentimen=='netral'): 
			label=2
		labels.append(label)
	return {'feature vector':featureVector,'labels':labels}

			
		
		
if __name__ == '__main__':
	fp = open('twiit.csv', 'r')
	line = fp.read()
	inpTweets = csv.reader(open('twiit.csv', 'rb'), delimiter=';', quotechar='|')
	pre=preprocessing.preprocess(line)
	fitur=preprocessing.get_fitur(pre)
	getSVMFeatureLabel(inpTweets,fitur)
	preprocessing.fitur_ekstraksi(inpTweets)
	print preprocessing.get_fitur(pre)
