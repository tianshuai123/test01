import streamlit as st
from datetime import time, datetime


st.header('st.slider')

st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write(f"I'm {age} years old")
