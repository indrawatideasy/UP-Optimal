#import libraries
import streamlit as st
import numpy as np
import pandas as pd
import xgboost as xgb
import pickle
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

#import the data
data = pd.read_csv("https://raw.githubusercontent.com/indrawatideasy/profil-pemda/main/pengelolaangup.csv")

def load_model('model_baggingclf.pkl'):
	loaded_model = pickle.load('model_baggingclf.pkl', 'rb')
	return loaded_model
	
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

feature_list = [UP, PAGU, REALISASI, PAGU52, REAL52, PAGU53, REAL53]
single_pred = np.array(feature_list)

#checking prediction 
if st.button("Prediksi"):
	
	loaded_model = load_model('model_baggingclf.pkl')
	prediction = loaded_model.predict(single_pred)
	st.success(f"{prediction.item().title()}")
