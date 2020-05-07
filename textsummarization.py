from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
import numpy

#! /usr/bin/env python
# -*- coding: utf-8 -*-



stopwords = stopwords.words('english')
import pandas as pd

def text_summarization(text,percentage=1/4):
	documents = sent_tokenize(text)
	vectorizer = TfidfVectorizer(stop_words = stopwords,encoding = 'utf-8')
	tf_idf = vectorizer.fit(documents)
	tf_idf =  vectorizer.transform(documents)

	tf_idf_values = []
	df = pd.DataFrame(tf_idf.toarray(),columns = vectorizer.get_feature_names())
	for x in range(df.shape[0]):
		print(sum(df.iloc[x,:]))
		tf_idf_values.append(sum(df.iloc[x,:]))
	tf_idf_mean = sum(tf_idf_values)/len(tf_idf_values)
	important_sentences_id = []
	for x in range(len(tf_idf_values)):
		if tf_idf_values[x] >= (1-percentage)*max(tf_idf_values):
			important_sentences_id.append(x)
	new_text = ''
	for x in important_sentences_id:
		new_text = new_text + documents[x]


if __name__ == "__main__": 
	text_summarization('your text here')
