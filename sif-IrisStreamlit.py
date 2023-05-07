#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import streamlit as st
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.svm import SVC
from sklearn import tree
import seaborn as sns

iris = pd.read_csv('iris.csv')

X = iris[["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"]]
y = iris[["Species"]]

st.subheader('Classic Flower Classification Problem')

a = st.text_input("Your name")

st.write(f'Hello {a} \n We will solve the classification problem. We will need few inputs from you')

Sepal_length = st.slider("Sepal Length", min_value=iris.SepalLengthCm.min(), max_value=iris.SepalLengthCm.max())

Sepal_width = st.slider("Sepal Width", min_value=iris.SepalWidthCm.min(), max_value=iris.SepalWidthCm.max())

Petal_length = st.slider("Petal Length", min_value=iris.PetalLengthCm.min(), max_value=iris.PetalLengthCm.max())

Petal_width = st.slider("Petal Width", min_value=iris.PetalWidthCm.min(), max_value=iris.PetalWidthCm.max())

X_train = pd.DataFrame({'SepalLengthCm':[Sepal_length],
                       'SepalWidthCm':[Sepal_width],
                       'PetalLengthCm':[Petal_length],
                       'PetalWidthCm':[Petal_width]})

selectbox = st.sidebar.selectbox(
    'Please select your favourite model',
    ('DecisionTree', 'AdaBoost', 'SVC')
)

if selectbox == "DecisionTree":
    model_s = DecisionTreeClassifier(criterion = 'entropy', random_state=1234)
elif selectbox == "AdaBoost":
    model_s = AdaBoostClassifier(n_estimators=50, learning_rate=1, random_state=0)
else:
    svc=SVC(probability=True, kernel='linear')
    model_s = AdaBoostClassifier(n_estimators=50, base_estimator=svc,learning_rate=1, random_state=0)

model = model_s.fit(X,y)

y_pred = model.predict(X_train)

st.write("The Model Prediction is :" , y_pred)

