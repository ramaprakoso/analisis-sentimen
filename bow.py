import preprocessing
import csv
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.feature_extraction.text import TfidfVectorizer 

myvocab=['ahli','anggun','ganteng','santun','cocok']
"""
bahan=[
	'ahok ahli dan anggun dalam menangani masalah',
	'anis santun tapi tidak ahli dalam memimpin',
	'anggun adalah seorang artis yang anggun dan cocok untuk menjadi ahli masak'
	'anis','santun', 'tapi', 'tidak', 'ahli', 'dalam', 'memimpin',
	'anggun','adalah','seorang','artis','yang','anggun','dan','cocok','untuk','menjadi','ahli','masak'
	'ahok', 'ahli', 'dan', 'anggun', 'dalam', 'menangani' ,'masalah'
]
"""
inpTweets = csv.reader(open('twiit.csv', 'rb'), delimiter=';', quotechar='|')
ekstraksi_fitur=preprocessing.fitur_ekstraksi(inpTweets)
vectorizer=TfidfVectorizer(input='content')


vektor=CountVectorizer(vocabulary=myvocab)
#open file 
fp = open('tweet3000.csv', 'r')
tweet=fp.read()
#preprocess tweet
pre=preprocessing.preprocess(tweet)
#get fitur 
fitur=preprocessing.get_fitur(pre)
