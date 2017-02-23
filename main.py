import preprocessing 
import csv 

#file yang dibuka
with open('datafix/ahok.csv','r') as f:
	tweet=f.read()
	tweet=preprocessing.preprocess(tweet)
#file yang ditulis tidak usah bikin nama filnya kalau write dia nulis sendiri 
with open('datafix/ahokbersih.csv','w') as fp : 
	fp.write(tweet)
	fp.close()
