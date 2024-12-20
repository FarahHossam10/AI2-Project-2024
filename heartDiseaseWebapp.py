# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 20:49:58 2024

@author: hp
"""

import numpy as np
import pickle
import streamlit as st

#loaded_model = pickle.load(open("C:/Users/hp/Desktop/AI2-Project/trained_model.sav", "rb"))
loaded_model = pickle.load(open("C:/Users/hp/Desktop/AI2-Project/trained_model2.sav", "rb"))

def model_prediction(input_data):
    input_data_array = np.asarray(input_data)
    input_reshaped = input_data_array.reshape(1, -1)
    prediction = loaded_model.predict(input_reshaped)
    print(prediction)
    if(prediction[0] == 0):
        return "Person doesn't have risk of heart disease!"
    else:
        return "Person has risk!"
    
    
def main():
    st.title("Heart Disease Prediction App")
    #Age Sex ChestPainType Cholesterol	FastingBS	MaxHR	ExerciseAngina	Oldpeak	ST_Slope	
    Age = st.text_input("Patient's Age")
    Gender = st.text_input("Patient's Gender: 1 for Male, 0 for Female")
    ChestPainType = st.text_input("Patient's ChestPainType: 0 for ASY, 1 for ATA, 2 for NAP, 3 for TA")
    Cholesterol = st.text_input("Patient's Cholesterol")
    FastingBS = st.text_input("Patient's FastingBS")
    MaxHR = st.text_input("Patient's MaxHR")
    ExerciseAngina = st.text_input("Patient's ExerciseAngina: 0 for No, 1 for Yes")
    Oldpeak = st.text_input("Patient's Oldpeak")
    ST_Slope = st.text_input("Patient's ST_Slope: 1 for Flat, 2 for Up, 3 for Down")
    
    diagnosis = ''
    
    if st.button("Predict"):
        diagnosis = model_prediction([float(Age), int(Gender), int(ChestPainType), float(Cholesterol), int(FastingBS), float(MaxHR), int(ExerciseAngina), float(Oldpeak), int(ST_Slope)])
        
        if(diagnosis == "Person has risk!"):
            st.write("**:red[Person has risk!]**")
        else:
            st.write("**:green[Person doesn't have risk of heart disease!]**")
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    