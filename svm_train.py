from sklearn.feature_extraction.text import TfidfVectorizer 

vocabulary = "a list of words I want to look for in the documents".split()
vect = TfidfVectorizer(sublinear_tf=True, max_df=0.5, analyzer='word', 
           stop_words='english', vocabulary=vocabulary)

vect.fit(corpus)
vect.fit(corpus)
corpus_tf_idf = vect.transform(corpus) 

print corpus_tf_idf
