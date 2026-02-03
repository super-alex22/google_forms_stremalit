import streamlit as st
st.write("This is a geography quiz. Let's see how good your skills are")
st.write("I'd like humbly have you requested to enter your name here")
name = st.text_input("Have your name stated here")
gender = st.radio("Gender", ["Male", "Female", "Other", "Custom", "Prefer not to be shared"])
if gender == "Custom":
  gender_custom = st.text_input("Kindly have your gender stated here")
  st.write("Have me considered as")
  gender_custom_type = st.radio("Gender", ["Male", "Female", "Other"])
age = st.number_input("Kindly have your age stated here")
if age<1:
  st.error("You haven't been born yet. See you back when you are")
