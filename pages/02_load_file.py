import streamlit as st

st.header("escolher arquivo")

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)