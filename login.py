import streamlit as st
import pandas as pd
import numpy as np


# st.image('login_right_img.png', caption='Sunrise by the mountains')
st.subheader('Qnaboat', divider='rainbow')
st.title(':blue[login]')

col1, col2 = st.columns([0.7, 0.3])
with col1:

    email = st.text_input('Email',placeholder="enter your email")

    password = st.text_input('Password',placeholder="enter correct password")

def values():
    if email and password:
        st.write('email : ', email)
        st.write('password : ', password)
st.button("login", type="primary",on_click=values())
st.markdown("[forgot password ?](#section-1)")
st.markdown("[register for new user ?](#section-1)")


