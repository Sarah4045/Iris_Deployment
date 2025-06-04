import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import streamlit as st
iris= datasets.load_iris()
x = iris.data
y = iris.target

rfc = RandomForestClassifier()
rfc.fit(x,y)

st.write(""" # simple prediction iris Flowers App! """)
st.sidebar.header("Input Parameters")

def User_input():
    first=st.sidebar.slider('Sepal_lenght',4.3,7.9,5.4)
    second=st.sidebar.slider('Sepal_Width',2.5,4.4,3.4)
    third=st.sidebar.slider('Petal_Length',1.0,6.9,1.3)
    forth=st.sidebar.slider('Petal_Width',0.1,2.5,0.2)

    data={'Sepal_lenght':first,
          'Sepal_Width' : second,
          'Petal_Length' : third,
          'Petal_Width': forth}
    Features= pd.DataFrame(data,index=[0])

    return Features

df = User_input()

st.subheader("User Inputs Parameters")
st.write(df)

st.subheader('Target Names')
st.write(iris.target_names)

pre = rfc.predict(df)
pro = rfc.predict_proba(df)

st.subheader('Prediction')
st.write(iris.target_names[pre])

st.subheader('Prediction_Proba')
st.write(pro)