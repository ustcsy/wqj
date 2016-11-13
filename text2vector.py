#!/usr/bin/python

text_arr = []
infile = open('../data/res_stem.corpus','r')
line_cnt = 0
tmp_line = infile.readline().strip()
while tmp_line:
    print line_cnt
    text_arr.insert(line_cnt, tmp_line)
    line_cnt = line_cnt+1
    tmp_line = infile.readline().strip()
infile.close()
print text_arr
'''
from sklearn.feature_extraction.text import CountVectorizer

count_vectorizer = CountVectorizer(min_df=1)
term_freq_matrix = count_vectorizer.fit_transform(text_arr)
print "Vocabulary:", count_vectorizer.vocabulary_

from sklearn.feature_extraction.text import TfidfTransformer

tfidf = TfidfTransformer(norm="l2")
tfidf.fit(term_freq_matrix)

tf_idf_matrix = tfidf.transform(term_freq_matrix)
print tf_idf_matrix.todense()
'''
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vectorizer = TfidfVectorizer(min_df = 350)
tfidf_matrix = tfidf_vectorizer.fit_transform(text_arr)

vec_matrix = tfidf_matrix.todense()
print vec_matrix.shape
'''
outfile = open("christmas_job_music_stream/vector_chrisrmas_job_music","w")
for i in range(0,line_cnt-1):
    outfile.write(vec_matrix[i])
    outfile.write("\n")
outfile.close()
'''
import numpy
numpy.savetxt('../data/res.vector', vec_matrix, delimiter=',')
