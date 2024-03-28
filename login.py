import streamlit as st
import pandas as pd
import numpy as np


st.image('login_right_img.png', caption='Sunrise by the mountains')
st.sidebar.header('Qnaboat', divider='rainbow')
st.sidebar.title(':blue[login]')

email = st.sidebar.text_input('Email', 'enter your email')

password = st.sidebar.text_input('Password', 'enter correct password')

st.sidebar.button("login", type="primary")

st.sidebar.markdown("[forgot password ?](#section-1)")
st.sidebar.markdown("[register for new user ?](#section-1)")
