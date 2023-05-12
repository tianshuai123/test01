# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt


st.header('st.write')

st.markdown('Hello, World!')
st.header('Hello, World!')
st.subheader('Hello, World!')
st.caption('Hello, World!')
st.text('Hello, World!')
st.latex('Hello, World!')
st.code('Hello, World!')
st.write('Hello, World!')


st.write('Hello, *World!* :sunglasses:')
st.write(1234)

df = pd.DataFrame({
    'first_column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })
st.write(df)

st.write('Below is a DataFrame: ', df)

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
