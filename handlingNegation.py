def negate_sequence(text):
    negation = False
    delims = "?.,!:;"
    result = []
    words = text.split()
    prev = None
    pprev = None
    for word in words:
        stripped = word.strip(delims).lower()
        negated = "not_" + stripped if negation else stripped
        result.append(negated)
        if prev:
            bigram = prev + " " + negated
            result.append(bigram)
            if pprev:
                trigram = pprev + " " + bigram
                result.append(trigram)
            pprev = prev
        prev = negated

        if any(neg in word for neg in ["not", "n't", "no"]):
            negation = not negation

        if any(c in word for c in delims):
            negation = False

    return result

if __name__ == '__main__': 
	text=[   'i',
    'am',
    'i am',
    'not',
    'am not',
    'i am not',
    'not_happy',
    'not not_happy',
    'am not not_happy',
    'not_today',
    'not_happy not_today',
    'not not_happy not_today',
    'and',
    'not_today and',
    'not_happy not_today and',
    'i',
    'and i',
    'not_today and i',
    'am',
    'i am',
    'and i am',
    'not',
    'am not',
    'i am not',
    'not_feeling',
    'not not_feeling',
    'am not not_feeling',
    'not_well',
    'not_feeling not_well',
    'not not_feeling not_well']
	print negate_sequence(text)
