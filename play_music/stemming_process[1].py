#Stemming and Lemmatization

from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer
porter = PorterStemmer()
lancaster = LancasterStemmer()
snowball = SnowballStemmer('english')

words = ['describe', 'describes', 'discription', 'discriptions', 'eat', 'eating', 'eats', 'ate', 'run', 'ran', 'runs', 'running', 'tokenize', 'tokenizer', 'tokenization']
for x in words:
	print(x, porter.stem(x), lancaster.stem(x), snowball.stem(x))
