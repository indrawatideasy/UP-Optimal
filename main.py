#import libraries
import streamlit as st
import pandas as pd
import xgboost as xgb
from sklearn import datasets

#Loading up the Regression model we created
model = xgb.XGBRegressor()
model.load_model('model_sklearn.json')

#Apps Title
st.write("""
# UP OPTIMA
Aplikasi Prediksi Nilai UP Optimal Satker Lingkup Kanwil DJPB Sumsel
""")

#Sidebar
st.sidebar.header('Masukkan Parameter')

def user_input_features():
    sepal_length = st.sidebar.number_input('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.number_input('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.number_input('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.number_input('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features
    
#User Input Parameter
df = user_input_features()

#Subheader
st.subheader('Hasil Masukan Parameter')
st.write(df)

iris = datasets.load_iris()
X = iris.data
Y = iris.target

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Prediksi Realisasi GUP')
st.write(iris.target_names[prediction])
#st.write(prediction)
