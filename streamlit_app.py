# -*- coding: utf-8 -*-

import streamlit as st
from datetime import time, datetime


st.header('st.slider')

st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write(f"I'm {age} years old")


st.subheader('Range slider')

values = st.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0))
st.write('Values: ', values)
