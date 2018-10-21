# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 15:45:20 2018

@author: admin
"""

from sklearn.externals import joblib
import numpy as np 
import os

model = joblib.load('exp/k_means/pretrained_model.joblib') 


def load_features(src):
    print("[+] Load data....")
    data = []
    for folder in os.listdir(src):
        folder_path = os.path.join(src, folder) #take path       
        for file in os.listdir(folder_path):
            data.append(np.load(os.path.join(folder_path, file))[0])
    print("[+] Load data finished")
    return data

src = 'features/vgg16_fc2/testing'
data_test = load_features(src)

result = model.predict(data_test)
print('result : ', result)


