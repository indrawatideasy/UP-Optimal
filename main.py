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
kode_satker = st.number_input("berapa kode satkernya?",int(data.SATKER.min()),int(data.SATKER.max()),int(data.SATKER.mean()))

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
predictions = (round(value) for value in y_pred)

#checking prediction 
if st.button("Prediksi"):
    st.success("Prediksi Realisasi GUP yaitu Rp {}. "format(int(predictions[0])))
