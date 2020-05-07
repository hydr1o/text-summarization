from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
import numpy
import math
#! /usr/bin/env python
# -*- coding: utf-8 -*-
stopwords = stopwords.words('english')
import pandas as pd
class TextSummarization:
	def __init__(self,text,percentage=1/4,encoding='utf-8'):
		self.text = text
		self.percentage = percentage
		self.encoding = encoding
	def summarize(self):
		documents = sent_tokenize(self.text)
		vectorizer = TfidfVectorizer(stop_words = stopwords,encoding = self.encoding)
		tf_idf = vectorizer.fit(documents)
		tf_idf =  vectorizer.transform(documents)
		tf_idf_values = []
		self.df = pd.DataFrame(tf_idf.toarray(),columns = vectorizer.get_feature_names())
		
		for x in range(self.df.shape[0]):
			tf_idf_values.append(sum(self.df.iloc[x,:]))
		tf_idf_mean = sum(tf_idf_values)/len(tf_idf_values)
		tf_idf_array = []
		for x in range(len(tf_idf_values)):
			tf_idf_array.append([documents[x],tf_idf_values[x]])
		sorted_array = sorted(tf_idf_array, key=lambda tup:(-tup[1], tup[0]),reverse=True)
		sorted_array = [s for s in sorted_array[len(sorted_array)-round(len(sorted_array)*self.percentage):len(sorted_array)]]
		output = []
		for x in range(len(sorted_array)):
			output.append(sorted_array[x][0])
		output_text = ''
		for x in output:
			output_text=output_text + str(x)
		return output_text
	def tf_idf_table(self):
		tokenized = sent_tokenize(self.text)
		vectorizer = TfidfVectorizer(stop_words = stopwords,encoding = self.encoding)
		tf_idf = vectorizer.fit(tokenized)
		tf_idf =  vectorizer.transform(tokenized)
		self.dataframe = pd.DataFrame(tf_idf.toarray(),columns = vectorizer.get_feature_names())
		return self.dataframe

if __name__ == "__main__": 
	text = TextSummarization('The COVID-19 pandemic, also known as the coronavirus pandemic, is an ongoing pandemic of coronavirus disease 2019 (COVID‑19) caused by severe acute respiratory syndrome coronavirus 2 (SARS‑CoV‑2).[6] The outbreak was identified in Wuhan, China, in December 2019.[4][7] The World Health Organization declared the outbreak a Public Health Emergency of International Concern on 30 January, and a pandemic on 11 March.[8][9] As of 7 May 2020, more than 3.77 million cases of COVID-19 have been reported in over 187 countries and territories, resulting in more than 264,000 deaths. More than 1.25 million people have recovered.[5]. The virus is primarily spread between people during close contact,[c] often via small droplets produced by coughing,[d] sneezing, and talking.[10][11][13] The droplets usually fall to the ground or onto surfaces rather than remaining in the air over long distances.[10] People may also become infected by touching a contaminated surface and then touching their face.[10][11] On surfaces, the amount of virus declines over time until it is insufficient to remain infectious, but it may be detected for hours or days.[10][13][14] It is most contagious during the first three days after the onset of symptoms, although spread may be possible before symptoms appear and in later stages of the disease.[15]. Common symptoms include fever, cough, fatigue, shortness of breath, and loss of smell.[10][16][17] Complications may include pneumonia and acute respiratory distress syndrome.[18] The time from exposure to onset of symptoms is typically around five days, but may range from two to fourteen days.[19][20] There is no known vaccine or specific antiviral treatment.[10] Primary treatment is symptomatic and supportive therapy.[21]. Recommended preventive measures include hand washing, covering one\'s mouth when coughing, maintaining distance from other people, wearing a face mask in public settings, and monitoring and self-isolation for people who suspect they are infected.[10][22] Authorities worldwide have responded by implementing travel restrictions, lockdowns, workplace hazard controls, and facility closures. Many places have also worked to increase testing capacity and trace contacts of infected persons. The pandemic has caused severe global socioeconomic disruption,[23] including the largest global recession since the Great Depression.[24] It has led to the postponement or cancellation of sporting, religious, political and cultural events,[25] widespread supply shortages exacerbated by panic buying,[26][27] and decreased emissions of pollutants and greenhouse gases.[28][29] Schools, universities and colleges have closed either on a nationwide or local basis in 194 countries, affecting approximately 98.5 per cent of the world\'s student population.[30] Misinformation about the virus has spread online,[31] and there have been incidents of xenophobia and discrimination against Chinese people and against those perceived as being Chinese, or as being from areas with high infection rates.[32][33][34]')
	print(text.tf_idf_table())


