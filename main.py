#import libraries
import streamlit as st
import numpy as np
import pandas as pd
import pickle
import xgboost as xgb
import joblib as joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

#Loading up the Regression model we created
df = pd.read_csv("pengelolaangup.csv")
model = joblib.load('pred_realgup.pkl')

#Caching the model for faster loading
@st.cache

# Define the prediction function
def predict(UP, PAGU, REALISASI, PAGU52, REAL52, PAGU53, REAL53):
	prediction = model.predict(pd.DataFrame([[UP, PAGU, REALISASI, PAGU52, REAL52, PAGU53, REAL53]], columns=['UP', 'PAGU', 'REALISASI', 'PAGU52', 'REAL52', 'PAGU53', 'REAL53']))
	return prediction

#Apps Title
st.write("""
# UP OPTIMAL
Aplikasi Prediksi Nilai UP Optimal Satker Lingkup Kanwil DJPB Sumsel
""")

#input the numbers
UP = st.number_input('UP:', min_value=1.0, max_value=10000000000.0, value=1.0)
PAGU = st.number_input('PAGU:', min_value=1.0, max_value=10000000000.0, value=1.0)
REALISASI = st.number_input('REALISASI:', min_value=1.0, max_value=10000000000.0, value=1.0)
PAGU52 = st.number_input('PAGU52:', min_value=1.0, max_value=10000000000.0, value=1.0)
REAL52 = st.number_input('REAL52:', min_value=1.0, max_value=10000000000.0, value=1.0)
PAGU53 = st.number_input('PAGU53:', min_value=1.0, max_value=10000000000.0, value=1.0)
REAL53 = st.number_input('REAL53:', min_value=1.0, max_value=10000000000.0, value=1.0)

#checking prediction 
if st.button('Prediksi'):
    realgup = predict(UP, PAGU, REALISASI, PAGU52, REAL52, PAGU53, REAL53)
    st.success(f'Prediksi realisasi GUP yaitu ${realgup[0]:.2f} IDR')
