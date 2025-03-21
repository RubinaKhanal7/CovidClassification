import streamlit as st
import pandas as pd
import pickle as pk

st.title('Covid Classification')
st.image('https://www.iaea.org/sites/default/files/styles/2016_landing_page_banner_1140x300/public/images/hhc-covid19-banner.jpg?itok=HzkrewMn&timestamp=1600932831')

with open('Covid_Classification.pickle', 'rb') as filename:
    model = pk.load(filename)

#create form

Cough_symptoms = st.radio("Enter Cough_symptoms",[True,False])
Fever = st.radio("Enter Fever",[True,False])
Sore_throat = st.radio("Enter Sore_throat",[True,False])
Shortness_of_breath = st.radio("Enter Shortness_of_breath",[True,False])
Headache = st.radio("Enter Headache",[True,False])
Known_contact = st.selectbox("Pic the point of contact", ["Abroad", "Contact with confirmed","Other"])

d = {'Abroad':0,'Contact with confirmed':1,"Other":2}
df = pd.DataFrame(
    [[Cough_symptoms, Fever,Sore_throat, Shortness_of_breath, Headache, d[Known_contact]]],
    columns=['Cough_symptoms', 'Fever','Sore_throat', 'Shortness_of_breath', 'Headache', 'Known_contact']
)
if st.button("Predict"):
    result = model.predict(df)

    if int(result[0])==1:
        st.error(f"I am sorry to say that you have Covid. Result = {result[0]}")
    else:
        st.success(f"Thank god you don't have Covid. Result = {result[0]}")