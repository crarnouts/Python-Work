# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 14:22:46 2019

@author: arnou
"""

# core
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn

# ml
from sklearn import datasets as ds
from sklearn import linear_model as lm
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.model_selection import train_test_split as tts


df = pd.read_csv("breast-cancer-wisconsin-data.data")

df = pd.read_csv("http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv")