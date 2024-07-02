import os 
import sys 
import pickle 
import pandas as pd 
import numpy as np  
import streamlit as st 
from sklearn.tree  import DecisionTreeClassifier  


model_path = os.path.join('artifacts','model.pkl')
model = pickle.load(open(model_path,'rb'))   

st.markdown("<h1 style='text-align: center; color: red;'>Heart Disease Detector</h1>", unsafe_allow_html=True)
st.markdown('----------------------------------------------------------------') 

#age,gender,impluse,pressurehight,pressurelow,glucose,kcm,troponin,
col1, col2, col3 ,col4 = st.columns(4) 

with col1:
   age = st.number_input('Enter Age',min_value=0,max_value=120)
   gender = st.selectbox('Select Gender',('Male','Female')) 

with col2:
   pressurehight = st.number_input('Enter Pressure High')
   pressurelow = st.number_input('Enter Pressure Low') 
   

with col3:
   impluse = st.number_input('Enter Impluse')
   glucose = st.number_input('Enter Glucose') 

with col4: 
   kcm = st.number_input('Enter Kcm')
   troponin = st.number_input('Enter Troponin')   
if gender == 'Female':
   gender = 0
elif gender == 'Male':
   gender = 1 

if st.button(label='Predict'):
   if age != 0 and pressurehight !=0 and pressurelow !=0 and  impluse !=0 and glucose != 0 :
      data = pd.DataFrame(np.asarray([age,gender,impluse,pressurehight,pressurelow,glucose,kcm,troponin]).reshape(1,-1),
                          columns=['age','gender','impluse','pressurehight','pressurelow','glucose','kcm','troponin'])  
      result = model.predict(data)  
 
      if result[0] == 0 :
         st.success('You do not have heart disease')
   
      elif result[0] == 1 : 
         st.error('You have heart disease')
         if glucose < 70 or  glucose > 100 :
            st.header('Warnings')
            st.error('You have abnormal Glucose Levels') 
            st.write('Please rech the doctor')       
      
   

   else :
      st.error('Please fill all the fields') 
   


      