#import libraries
import streamlit as st
import numpy as np
import pandas as pd
import pickle
import joblib as joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

#import the data
df = pd.read_csv("pengelolaangup.csv")
model = joblib.load('pred_realgup.pkl')
def predict(UP, PAGU, REALISASI, PAGU52, REAL52, PAGU53, REAL53):
	prediction=model.predict([[UP, PAGU, REALISASI, PAGU52, REAL52, PAGU53, REAL53]])
	return prediction

#Apps Title
st.write("""
# UP OPTIMAL
Aplikasi Prediksi Nilai UP Optimal Satker Lingkup Kanwil DJPB Sumsel
""")

#input the numbers
df_pred = pd.DataFrame(columns= ['UP', 'PAGU', 'REALISASI', 'PAGU52', 'REAL52', 'PAGU53', 'REAL53'])
df_pred['UP'] = st.number_input("Nilai UP", 1, 100000000000)
df_pred['PAGU'] = st.number_input("Nilai PAGU", 1, 100000000000)
df_pred['REALISASI'] = st.number_input("Nilai REALISASI", 1, 100000000000)
df_pred['PAGU52'] = st.number_input("Nilai PAGU52", 1, 100000000000)
df_pred['REAL52'] = st.number_input("Nilai REAL52", 1, 100000000000)
df_pred['PAGU53'] = st.number_input("Nilai PAGU53", 1, 100000000000)
df_pred['REAL53'] = st.number_input("Nilai REAL53", 1, 100000000000)

#checking prediction 
if st.button("Predict"):
	result=predict('UP', 'PAGU', 'REALISASI', 'PAGU52', 'REAL52', 'PAGU53', 'REAL53')
	st.success("Prediksi realisasi GUP yaitu{}.".format(result))
