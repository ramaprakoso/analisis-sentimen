import re,string
from nltk.tokenize import word_tokenize
filename='tweet1clean.csv'
sname='stopword.txt'
def preprocess(tweet):
	#hapus url 
	tweet=hapus_url(tweet) 
	#hapus tandabaca
	tweet=hapus_tanda(tweet)
	#hapus angka 
	tweet=hapus_angka(tweet)
	#token 
	tokens=tokenize(tweet)
	tokens=kbbi(tokens)
	#tokens=['ciuman','mencuri','membelanjakan','mempekerjakan','melayani','mengatur','merasakan','memeriksa']
	dasar=[line.strip('\n')for line in open('kamus/rootword.txt')]
	nonKataDasar=list(set(tokens)-set(dasar))
	kataDasar=list(set(tokens)-set(nonKataDasar))
	for i in range(0,len(nonKataDasar)): 
		nonKataDasar[i]=stemming(nonKataDasar[i],dasar)
	tokens=list(set(nonKataDasar+kataDasar))
	#tokens=stopwordDel(token)	
	return tokens   
def hapus_url(tweet): 
	url=re.sub(r'http\S',"",tweet)
	return url 
def hapus_tanda(tweet):
	tb=re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)","",tweet)
	return tb
def hapus_angka(tweet): 
	angka=re.sub(r'\w*\d\w*', '',tweet).strip()
	return angka 
def tokenize(tweet): 
	token=word_tokenize(tweet)
	return token 
def stopwordDel(token):
	stopword=[word.strip('\n') for word in open('kamus/stopword.txt')] 
	noise=[noise.strip('\n').strip('\r') for noise in open('kamus/noise.txt')]
	tampung=[]
	for i in range(0,len(token)): 
		if token[i] not in stopword: 
			tampung.append(token[i])
	return tampung
def kbbi(token): 
	kbba=[kamus.strip('\n').strip('\r') for kamus in open('kamus/kbba.txt')]
	#ubah list menjadi dictionary 
	dic={}
	for i in kbba: 
		(key,val)=i.split('\t')
		dic[str(key)]=val
	#kbbi cocokan 
	final_string = ' '.join(str(dic.get(word, word)) for word in token).split()
	return final_string
#stemming kata 
def akhiranPertama(token): 
	#menghapus -kah,-lah,-tah,-pun
	if re.search('(a-z0-9)+kah$',token): 
		token=re.sub(r'(a-zO-9)+kah$',r'\1',token)
		return token 
	if re.search('(a-z0-9)+lah$',token): 
		token=re.sub(r'(a-zO-9)+lah$',r'\1',token)
		return token 
	if re.search('(a-z0-9)+tah$',token): 
		token=re.sub(r'(a-zO-9)+tah$',r'\1',token)
		return token 
	if re.search('(a-z0-9)+pun$',token): 
		token=re.sub(r'(a-zO-9)+pun$',r'\1',token)
		return token 
	return token 
def akhiranKedua(token): 
	#fungsi stemming menghapus kata ganti milik -ku,-mu,-ya
	if re.search('([a-z0-9]+)nya$',token):
		token=re.sub(r'([a-z0-9]+)nya$','r\1',token)
		return token 
	if re.search('([a-z0-9]+)ku$',token):
		token=re.sub(r'([a-z0-9]+)ku$','r\1',token)
		return token 
	if re.search('([a-z0-9]+)mu$',token):
		token=re.sub(r'([a-z0-9]+)mu$','r\1',token)
		return token 
	return token 
def akhiranKetiga(token): 
	if re.search(r'([a-z0-9]+)kan$',token): 
		token=re.sub(r'([a-z0-9]+)kan$','r\1',token)
		return token 
	if re.search(r'([a-z0-9]+)an$',token): 
		token=re.sub(r'([a-z0-9]+)an$','r\1',token)
		return token 
	if re.search(r'([a-z0-9]+)i$',token): 
		token=re.sub(r'([a-z0-9]+)i$','r\1',token)
		return token 
	return token 
def awalanPertama(token):
	#menghapus awalan me-,pe-,di-,ter-,ke-
	if re.search('^meng',token): 
		token=re.sub('^meng','',token)
		return token 
	if re.search('^meny',token):
		 token=re.sub('^meny','s',token)
		 return token 
	if re.search('^men',token): 
		token=re.sub('^men','',token) 
		return token
	if re.search('^me',token): 
		token=re.sub('^me','',token)
		if re.search('^m(^[aiueo])',token): 
			token=re.sub('^m([^aiueo])',r'\1',token)
		return token
	if re.search('^peng',token): 
		token=re.sub('^peng','',token)
		return token 
	if re.search('^peny',token): 
		token=re.sub('^peny','s',token)
		return token 
	if re.search('^pen',token): 
		token=re.sub('^pen','',token)
		return token 
	if re.search('^pem',token): 
		if re.search('^pem[aiueo]',token): 
			token=re.sub('^pem','p',token)
		else: 
			token=re.sub('^pem','',token)
		return token 
	if re.search('^di',token):
		token=re.sub('^di','',token)
		return token 
	if re.search('^ter',token): 
		token=re.sub('^ter','',token)
		return token 
	if re.search('^ke',token): 
		token=re.sub('^ke','',token)
		return token 
	return token 
def awalanKedua(token): 
	if re.search('^ber',token): 
		token=re.sub('^ber','',token)
		return token 
	if re.search('^belajar',token):
		token=re.sub('^belajar','ajar',token)
		return token 
	
	#if re.search('^bek+er',token): 
	#	token=re.sub('^bek+er','ker',token)
	#	return token 
	if re.search('^per',token):
		token=re.sub('^per','',token)
		return token 
	if re.search('^pelajar',token): 
		token=re.sub('^pelajar','ajar',token)
		return token 
	if re.search('^pe',token): 
		token=re.sub('^pe','',token)
		return token
	return token  
def stemming(token,dasar):
		#menghapus akhiran -kah, -lah, -tahs
		token=akhiranPertama(token)
		if token in dasar: 
			return token 
		#mengganti kepemilikan kata -ku -mu -nya 
		token=akhiranKedua(token)
		if token in dasar: 
			return token 
			
		tempToken=token 
		token=awalanPertama(token)
		if token in dasar: 
			return token 
		if tempToken==token: 
			token=awalanKedua(token)
			if token in dasar: 
				return token 
			token=akhiranKetiga(token)
			if token in dasar: 
				return token 
		else: 
			temptoken2 = token
			token = akhiranKetiga(token)
			if token in dasar :
				return token
			if token != temptoken2:
				token = awalanKedua(token)
				if token in dasar :
					return token
		return token 
if __name__=='__main__': 
	with open(filename,"r") as f:
		data=f.read()
	
	print preprocess(data) 
			
			
			#stopwordDel()	
		
		
			
	"""
	def get_token(self,filename,fname):
		#open file tweet 
		with open(filename,"r") as f:
			data=f.read().split('\n')
			tampung=[]
			for text in data: 
				#remove url
				result=re.sub(r"http\S+", "", text)
				#remove number 
				result=re.sub(r'\w*\d\w*', '',result).strip()
				#remove punctuation 
				result=' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",result).split())
				tampung.append(result) 
			#stopword removing with token  
			stop=[unicode(x.strip(),'utf-8') for x in open(fname,'r').read().split('\n')]
			t=[]
			token=[word_tokenize(i) for i in tampung]
			for i in token: 
				for kata in i: 
					if kata not in stop: 
						t.append(kata)
			return t
		with open('kbba.txt','r') as k : 
			kbba=k.read().split('\n')	
			dic={}
			for i in kbba: 
				(key,val)=i.split('\t')
				dic[str(key)]=val
			u=[]
			for word in t: 
				for kandidat in dic: 
					if kandidat in word: 
						word=word.replace(kandidat,dic[kandidat])
				print word
			print u
		"""
