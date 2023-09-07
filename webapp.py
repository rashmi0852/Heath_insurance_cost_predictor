# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 19:54:51 2022

@author: rashmi
"""

import numpy as np
import pickle
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
import plotly.express as px


sns.set_style("darkgrid")




#loading the saved model
loaded_model=pickle.load(open("C:/Users/rashmi/Desktop/major/trained_model.sav","rb"))



#creating a function for prediction

def cost_prediction(input_data):
    
    #chaging imputdata as numpy array
    np_data=np.asarray(input_data)
    #reshape array
    data_reshape=np_data.reshape(1,-1)
    prediction=loaded_model.predict(data_reshape)
    return prediction
    
    
def prediction():
     #giving a title
     st.title("Health insurance cost predictor")
     #getting the input data from user
     age= st.text_input("Enter Your Age")
     
     sex=st.selectbox("Gender",options=["male","female"])
     bmi=st.text_input("Body Mass Index")
     childern=st.slider("No.Of childern",0,50,0)
     
     smoker=st.selectbox("Are u a Smoker?",options=["yes","no"])
     
     region=st.selectbox("Region", options=["SouthEast","SouthWest","NorthEast","NorthWest"])
     
     if sex == "male":
         sex2=1
     else:
         sex2=0
         
     if smoker == "yes":
         smoker2=1
     else:
         smoker2=0
         
     if region == "SouthEast":
         region2=2
     elif region == "SouthWest":
         region2=3
     elif region == "NorthEast":
         region2=0
     else:
         region=1
     
     
     
     
     
     
     #gender
     #code for prediction
     cost=''
    
     #creating a button
     if st.button("predict"):
         
         cost=cost_prediction([age,sex2,bmi,childern,smoker2,region2])
        
        
     st.write("predicted cost is $:")
     st.success(cost)
     
def explore():
    st.title("Explore...")
    df = pd.read_csv("insurance.csv")
    st.header("To see the dataset")
    check= st.checkbox("Click here")
    if check:
        
        st.dataframe(df)
    le_sex=LabelEncoder()
    df["sex"]=le_sex.fit_transform(df["sex"])
    
    
    le_smoker=LabelEncoder()
    df["smoker"]=le_smoker.fit_transform(df["smoker"])
    
    le_region=LabelEncoder()
    df["region"]=le_region.fit_transform(df["region"])
    st.header("Visualization")
    numeric_columns =list(df.select_dtypes(["float","int"]).columns)
    ck= st.checkbox("Click ")
    if ck:
        st.sidebar.subheader("visualization setting")
        x_values= st.sidebar.selectbox("x axis", options=numeric_columns)
        y_values= st.sidebar.selectbox("y axis", options=numeric_columns)
        plot=px.scatter(data_frame=df, x=x_values, y=y_values)
        st.plotly_chart(plot)
        
    
        
    
    

    
    
    
def main():
    
    
    data=st.sidebar.selectbox("Explore or Predict",("Explore","Predict"))
    if data == "Predict":
        prediction()
    else:
        explore()
    
   
    
        
    
if __name__=="__main__":
        main()


    
     



   
    
    
    
    
    
    
    