#import libraries
import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

#Apps Title
st.write("""
# UP OPTIMA
Aplikasi Prediksi Nilai UP Optimal Satker Lingkup Kanwil DJPB Sumsel
""")

#Sidebar
st.sidebar.header('Masukkan Parameter')
st.sidebar.number_input('Insert a number')

def user_input_features():
    sepal_length = number_input('Insert a number'),
    data = {'sepal_length': sepal_length,
            }
    features = pd.DataFrame(data, index=[0])
    return features

#User Input Parameter
df = user_input_features()

#Subheader
st.subheader('Hasil Masukan Parameter')
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

st.subheader('Prediksi Realisasi GUP')
st.write(iris.target_names[prediction])
#st.write(prediction)

#Prediction Probability
st.subheader('Prediction Probability')
st.write(prediction_proba)
