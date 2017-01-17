"""
def negasiHandling(text):
	kata_negatif=["korupsi","jahat","marah"]
	kata_positif=["bersih","sehat","bahagia"]
	delims="?.,!:;"
	result=[]
	positif=None
	negatif=None
	for kalimat in text: 
		kata=kalimat.split()
		negasi="tidak"+" "+kata
		if kata in kata_positif : 
			negasi=
		
		 
		
text=["ahok tidak korupsi","ahok tidak bersih"]
print negasiHandling(text)
"""
def negate_sequence(text):
    negation = False
    delims = "?.,!:;"
    result = []
    words = text.split()
    prev = None
    pprev = None
    for word in words:
        stripped = word.strip(delims).lower()
        negated = "tidak" + stripped if negation else stripped
        result.append(negated)
        if prev:
            bigram = prev + " " + negated
            result.append(bigram)
            if pprev:
                trigram = pprev + " " + bigram
                result.append(trigram)
            pprev = prev
        prev = negated

        if any(neg in word for neg in ["tidak", "bukan"]):
            negation = not negation

        if any(c in word for c in delims):
            negation = False

    return result


