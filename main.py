#import libraries
import streamlit as st
import pandas as pd
import xgboost as xgb
from sklearn import datasets

#Apps Title
st.write("""
# UP OPTIMA
Aplikasi Prediksi Nilai UP Optimal Satker Lingkup Kanwil DJPB Sumsel
""")

#Subheader


if st.button('Prediksi Realisasi GUP'):
    realgup = predict(UP, PAGU, REALISASI, PAGU52, REAL52, PAGU53, REAL53, STATUS)
    st.success(f'Prediksi nilai GUP yaitu sebesar Rp{realgup[0]:.2f} ')
