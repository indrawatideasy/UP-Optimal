#import libraries
import streamlit as st
import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

#import the data
data = pd.read_csv("https://raw.githubusercontent.com/indrawatideasy/profil-pemda/main/pengelolaangup.csv")

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

#splitting your data
X = data.drop('REALGUP', axis = 1)
y = data['REALGUP']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=.2, random_state=45)

#modelling step
#import your model
model = xgb.XGBRegressor()
#fitting and predict your model
model.fit(X_train, y_train)
y_pred = model.predict(X)

#checking prediction 
if st.button("Prediksi"):
    st.text("Prediksi Realisasi GUP yaitu Rp {}. ".format(int(y_pred[0])))
