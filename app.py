import streamlit as st
import joblib
st.title("SPAM HAM CLASSIFER")
text_model=joblib.load('spam-ham')
st.text_input("enter your message: ")
op=text_model.predict([ip])
if st.button('Predict'):
  st.title(op[0])
