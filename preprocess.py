#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import os
from nltk.stem.snowball import SnowballStemmer

# data regular
print 'clean the original tweet data into format ...'
raw_data_file = open('../data/res.txt', 'r')
clear_data_file = open('../data/res.data', 'w')
re_exp = r'^.+,\s.+,\s[0-9]+,\s.+$'
cnt = 1
for line in raw_data_file.readlines():
    print cnt, '\r',
    cnt = cnt+1
    line = line.strip(' \t\r\n')
    if re.match(re_exp, line):
        clear_data_file.write('\n')
    else:
        clear_data_file.write(' ')
    clear_data_file.write(line)
raw_data_file.close()
clear_data_file.close()
os.system('sed -i "" "1d" ../data/res.data')

# extract text
print 'extract tweet text from original tweet file ...'
clear_data_file = open('../data/res.data', 'r')
tweet_data_file = open('../data/res.corpus', 'w')
cnt = 1
for line in clear_data_file.readlines():
    print cnt, '\r',
    cnt = cnt+1
    arr_tmp = line.split(',', 4)
    tweet_tmp = arr_tmp[3].strip(' \t\r\n')
    tweet_data_file.write(tweet_tmp+'\n')
clear_data_file.close()
tweet_data_file.close()

# tweet corpus clean
print 'clean the tweet text corpus ...'
tweet_data_file = open('../data/res.corpus', 'r')
corpus_data_file = open('../data/res_clean.corpus', 'w')
re_url = re.compile(r'(https?:\/\/(?:www\.|(?!www))[^\s\.]+\.[^\s]{2,}|www\.[^\s]+\.[^\s]{2,})')    # remove url
re_at = re.compile(r'@[a-zA-z0-9_]+')   # remove @user
re_pattern = re.compile(r'[^a-zA-Z0-9\'\s]')    # remove non-number/english_char/number
re_blank = re.compile(r'[\s]+')     # remove multiple blank
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now", "rt", "re"]
cnt = 1
for line in tweet_data_file.readlines():
    print cnt, '\r',
    cnt = cnt+1
    # clear URL, @username, emoji
    line = re_url.sub(r'', line)
    line = re_at.sub(r'', line)
    line = re_pattern.sub(r' ', line)
    line = re_blank.sub(r' ', line)
    line = line.strip(' \t\r\n')
    # remove stop word
    arr_tmp = line.split(' ')
    for item_index, item in arr_tmp:
        if item in stop_word:
            arr_tmp.pop(item_index)
    line = ' '.join(arr_tmp)
    corpus_data_file.write(line+'\n')
tweet_data_file.close()
corpus_data_file.close()

# tweet text stem extract
print 'extract tweet text stem for machine learning ...'
stemmer = SnowballStemmer("english")
corpus_data_file = open('../data/res_clean.corpus', 'r')
stem_data_file = open('../data/res_stem.corpus', 'w')
line_cnt = 1
tmp_line = corpus_data_file.readline()
while tmp_line:
    print line_cnt
    line_cnt = line_cnt+1
    tmp_arr = tmp_line.split()
    i = 0
    while i < len(tmp_arr):
        tmp_arr[i] = stemmer.stem(tmp_arr[i])
        i = i+1
    tmp_line = " ".join(tmp_arr)
    stem_data_file.write(tmp_line)
    stem_data_file.write('\n')
    tmp_line = corpus_data_file.readline()
corpus_data_file.close()
stem_data_file.close()
