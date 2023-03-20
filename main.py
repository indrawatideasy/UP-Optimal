#import libraries
import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

#Apps Title
st.write("""
# Aplikasi Sederhana Prediksi Realisasi GUP Satker Lingkup Kanwil DJPB Prov. Sumsel""")

#Sidebar
st.sidebar.header('User Input Parameters')
st.number_input('masukkan nilai UP')

def user_input_features():
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'nilai_up': nilai_up,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

#User Input Parameter
df = user_input_features()

#Subheader
st.subheader('User Input parameters')
st.write(df)

iris = datasets.load_iris()
X = iris.data
Y = iris.target

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
st.write(iris.target_names)

st.subheader('Prediction')
st.write(iris.target_names[prediction])
#st.write(prediction)

#Prediction Probability
st.subheader('Prediction Probability')
st.write(prediction_proba)
