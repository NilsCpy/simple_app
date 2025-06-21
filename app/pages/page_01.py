import streamlit as st

secret_password = st.secrets["password"]

st.write('My password is : ' + secret_password)
