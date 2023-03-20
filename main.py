#import libraries
import streamlit as st
import pandas as pd
import xgboost as xgb
from sklearn import datasets

#import the data
data = pd.read_csv("https://raw.githubusercontent.com/indrawatideasy/profil-pemda/main/pengelolaangup.csv")

#Apps Title
st.write("""
# UP OPTIMA
Aplikasi Prediksi Nilai UP Optimal Satker Lingkup Kanwil DJPB Sumsel
""")

#input the numbers
nilai_up = st.number_input('UP')
nilai_pagu = st.number_input('PAGU')
nilai_real = st.number_input('REALISASI')
nilai_pagu52 = st.number_input('PAGU52')
nilai_real52 = st.number_input('REAL52')
nilai_pagu53 = st.number_input('PAGU53')
nilai_real53 = st.number_input('REAL53')

#splitting your data
X = data.drop('REALGUP', axis = 1)
y = data['REALGUP']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=.2, random_state=45)

#modelling step
#import your model
model=XGBRegressor()
#fitting and predict your model
model.fit(X_train, y_train)
model.predict(X_test)
errors = np.sqrt(mean_squared_error(y_test,model.predict(X_test)))
predictions = model.predict([[sqft_liv,bath,bed,floor]])[0]

if st.button('Prediksi Realisasi GUP'):
    realgup = predict(UP, PAGU, REALISASI, PAGU52, REAL52, PAGU53, REAL53, STATUS)
    st.success(f'Prediksi nilai GUP yaitu sebesar Rp{realgup[0]:.2f} ')
