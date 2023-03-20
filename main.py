#import libraries
import streamlit as st
import pandas as pd
import xgboost as xgb
from sklearn import datasets
from sklearn.model_selection import train_test_split

#import the data
data = pd.read_csv("https://raw.githubusercontent.com/indrawatideasy/profil-pemda/main/pengelolaangup.csv")

#Apps Title
st.write("""
# UP OPTIMA
Aplikasi Prediksi Nilai UP Optimal Satker Lingkup Kanwil DJPB Sumsel
""")

#input the numbers
nilai_up = st.number_input("Berapa nilai UP satker tahun sebelumnya?",int(data.UP())
nilai_pagu = st.number_input("PAGU", int())
nilai_real = st.number_input("REALISASI", int())
nilai_pagu52 = st.number_input(PAGU52, int())
nilai_real52 = st.number_input('REAL52', int())
nilai_pagu53 = st.number_input('PAGU53', int())
nilai_real53 = st.number_input('REAL53', int())

#splitting your data
X = data.drop('REALGUP', axis = 1)
y = data['REALGUP']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=.2, random_state=45)

#modelling step
#import your model
model = xgb.XGBRegressor()
#fitting and predict your model
model.fit(X_train, y_train)
model.predict(X_test)
errors = np.sqrt(mean_squared_error(y_test,model.predict(X_test)))
predictions = model.predict([[nilai_up, nilai_pagu, nilai_real, nilai_pagu52, nilai_real52, nilai_pagu53, nilai_real53]])[0]

#checking prediction 
if st.button("Prediksi"):
    st.header("Prediksi Realisasi GUP yaitu Rp {}".format(int(predictions)))
    st.subheader("Rentang prediksi nilai realisasi GUP yaitu Rp {} - Rp {}".format(int(predictions-errors),int(predictions+errors) ))
