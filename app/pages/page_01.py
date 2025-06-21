import streamlit as st

secret_password = st.secrets["password"]
local_secret_password = st.secrets["local_password"]

st.write('My password is : ' + secret_password)

st.write('My local password is : ' + local_secret_password)
