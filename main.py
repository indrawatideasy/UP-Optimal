#import libraries
import streamlit as st
import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

#import the data
data = pd.read_csv("pengelolaangup.csv")

#import model
model = joblib.load('pred_realgup.pkl')
prediction = model.predict(df_pred)
	
#Apps Title
st.write("""
# UP OPTIMAL
Aplikasi Prediksi Nilai UP Optimal Satker Lingkup Kanwil DJPB Sumsel
""")

#input the numbers
UP = st.number_input("Nilai UP", 1, 100000000000)
PAGU = st.number_input("Pagu", 1, 100000000000)
REALISASI = st.number_input("Realisasi", 1, 100000000000)
PAGU52 = st.number_input("Pagu Belanja Barang", 1, 100000000000)
REAL52 = st.number_input("Realisasi Belanja Barang", 1, 100000000000)
PAGU53 = st.number_input("Pagu Belanja Modal", 1, 100000000000)
REAL53 = st.number_input("Realisasi Belanja Modal", 1, 100000000000)

df_pred = pd.df([[UP, PAGU, REALISASI, PAGU52, REAL52, PAGU53, REAL53]],
		columns= ['UP', 'PAGU', 'REALISASI', 'PAGU52', 'REAL52', 'PAGU53', 'REAL53'])
df_pred['UP'] = df_pred['UP'].apply(lambda x: 1 if x == 'Male' else 0)
df_pred['PAGU'] = df_pred['PAGU'].apply(lambda x: 1 if x == 'Yes' else 0)
df_pred['REALISASI'] = df_pred['REALISASI'].apply(lambda x: 1 if x == 'Yes' else 0)
df_pred['PAGU52'] = df_pred['PAGU52'].apply(lambda x: 1 if x == 'Yes' else 0)
df_pred['REAL52'] = df_pred['REAL52'].apply(lambda x: 1 if x == 'Yes' else 0)
df_pred['PAGU53'] = df_pred['PAGU53'].apply(lambda x: 1 if x == 'Yes' else 0)
df_pred['REAL53'] = df_pred['REAL53'].apply(lambda x: 1 if x == 'Yes' else 0)
def transform(data):
    result = 3
    if(data=='High school diploma'):
        result = 0
    elif(data=='Undergraduate degree'):
        result = 1
    elif(data=='Postgraduate degree'):
        result = 2
    return(result)df_pred['education'] = df_pred['education'].apply(transform)

#checking prediction 
if st.button("Prediksi"):
	
	loaded_model = load_model('model.pkl')
	prediction = loaded_model.predict(single_pred)
	st.success(f"{prediction.item().title()}")
