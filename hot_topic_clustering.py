#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import metrics

# parameter
param = {
    'algorithm': 'DBSCAN'
}

# load data
tweet_vec = np.loadtxt('../data/res.vector', delimiter=',')

# cluster
if param['algorithm']=='DBSCAN':
    model = DBSCAN(eps=0.3, min_samples=10).fit(tweet_vec)
    np.savetxt('../data/res.topic', model.labels_, delimiter='\n')
