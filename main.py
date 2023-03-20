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
# UP OPTIMA
Aplikasi Prediksi Nilai UP Optimal Satker Lingkup Kanwil DJPB Sumsel
""")

#input the numbers
nilai_up = st.number_input("berapa nilai UP tahun sebelumnya?",int(data.UP.min()),int(data.UP.max()),int(data.UP.mean()))
nilai_pagu = st.number_input("berapa nilai PAGU tahun sebelumnya?",int(data.UP.min()),int(data.UP.max()),int(data.UP.mean()))
nilai_real = st.number_input("berapa nilai REALISASI tahun sebelumnya?",int(data.REALISASI.min()),int(data.REALISASI.max()),int(data.REALISASI.mean()))
nilai_pagu52 = st.number_input("berapa nilai PAGU52 tahun sebelumnya?",int(data.PAGU52.min()),int(data.PAGU52.max()),int(data.PAGU52.mean()))
nilai_real52 = st.number_input("berapa nilai REAL52 tahun sebelumnya?",int(data.REAL52.min()),int(data.REAL52.max()),int(data.REAL52.mean()))
nilai_pagu53 = st.number_input("berapa nilai PAGU53 tahun sebelumnya?",int(data.PAGU53.min()),int(data.PAGU53.max()),int(data.PAGU53.mean()))
nilai_real53 = st.number_input("berapa nilai REAL53 tahun sebelumnya?",int(data.REAL53.min()),int(data.REAL53.max()),int(data.REAL53.mean()))

#splitting your data
X = data.drop('REALGUP', axis = 1)
y = data['REALGUP']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=.2, random_state=45)

#modelling step
#import your model
model = xgb.XGBRegressor()
#fitting and predict your model
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
errors = np.sqrt(mean_squared_error(y_test,model.predict(X_test)))
predictions = [round(value) for value in y_pred]

#checking prediction 
if st.button("Prediksi"):
    st.header('Prediksi Realisasi GUP yaitu Rp {}'.format(predictions))
    st.subheader('Rentang prediksi nilai realisasi GUP yaitu Rp {} sd Rp {}'.format(predictions-errors),(predictions+errors))
