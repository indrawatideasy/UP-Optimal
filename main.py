#import libraries
import streamlit as st
import pandas as pd
import xgboost as xgb
from sklearn import datasets

#Loading up the Regression model we created
model = xgb.XGBRegressor()
model.load_model('model_sklearn.json')

#Now we do the predictions for cloned models and average them
def predict(self, X):
    predictions = np.column_stack([model.predict(X) for model in self.models_])
    return np.mean(predictions, axis=1)

#Apps Title
st.write("""
# UP OPTIMA
Aplikasi Prediksi Nilai UP Optimal Satker Lingkup Kanwil DJPB Sumsel
""")

#Sidebar
st.sidebar.header('Masukkan Parameter')

def user_input_features():
    nilai_up = st.sidebar.number_input('UP')
    nilai_pagu = st.sidebar.number_input('PAGU')
    nilai_realisasi = st.sidebar.number_input('REALISASI')
    nilai_pagu52 = st.sidebar.number_input('PAGU52')
    nilai_real52 = st.sidebar.number_input('REAL52')
    nilai_pagu53 = st.sidebar.number_input('PAGU53')
    nilai_real53 = st.sidebar.number_input('REAL53')
    nilai_status = st.sidebar.number_input('STATUS', 1, 0)
    data = {'UP': nilai_up,
            'PAGU': nilai_pagu,
            'REALISASI': nilai_realisasi,
            'PAGU52': nilai_pagu52}
    features = pd.DataFrame(data, index=[0])
    return features
    
#User Input Parameter
df = user_input_features()

#Subheader
st.subheader('Hasil Masukan Parameter')
st.write(df)

#st.write(prediction)
st.subheader('Prediction')
st.write(iris.target_names[predictions])
