# -*- coding: utf-8 -*-
"""pca_given_dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UWU8uJSQGYI6HnVM0RWt4c-V2BCVKFsf
"""

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import random

#loading the dat(aset
df=pd.read_csv("pca-demo-food-country.csv")

df.head()

df.info() #summary of dataset

df.drop(df.columns[0], axis=1, inplace=True) #removing the first columns
df

pca=PCA(n_components=2) #applying pca using sklearn
pca.fit(df)
new_data=pca.transform(df)

new_data_pca=pd.DataFrame(new_data,columns=["PC1","PC2"])

new_data_pca #new data after PCA