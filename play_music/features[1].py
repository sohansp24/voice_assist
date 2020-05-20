#Building a vocabulary from a input.

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(stop_words='english')
data = ['Stemming is the process of reducing inflection in words to their root.']
vectorizer.fit(data)

print(vectorizer.vocabulary_)
print(len(vectorizer.vocabulary_))
print(vectorizer.get_feature_names())

bow = vectorizer.transform(data)
print(bow.toarray())

