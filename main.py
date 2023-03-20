#import libraries
import streamlit as st
import pandas as pd
import xgboost as xgb
from sklearn import datasets

#import the data
data = pd.read_csv("https://raw.githubusercontent.com/indrawatideasy/profil-pemda/main/pengelolaangup_train.csv")

#Apps Title
st.write("""
# UP OPTIMA
Aplikasi Prediksi Nilai UP Optimal Satker Lingkup Kanwil DJPB Sumsel
""")

#input the numbers
nilai_up = st.slider('UP')

#Subheader

if st.button('Prediksi Realisasi GUP'):
    realgup = predict(UP, PAGU, REALISASI, PAGU52, REAL52, PAGU53, REAL53, STATUS)
    st.success(f'Prediksi nilai GUP yaitu sebesar Rp{realgup[0]:.2f} ')
