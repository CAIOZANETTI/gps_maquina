import streamlit as st
import pandas as pd

st.header("escolher arquivo formato parquet para primeira extração BRONZE")


files = [
	#'data/silver_jcb_relatorio_2022.parquet',
	'data/bronze_jcb_relatorio_2022.parquet',
	]

st.selectbox('files',files,key='file')	
#uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)

tab1,tab2,ta3 = st.tabs(['dataframe','describe','size'])

try:
	df = pd.read_parquet(st.session_state['file'],engine='pyarrow')
except:
	df = pd.read_parquet(st.session_state['file'],engine='fastparquet')

with tab1:
	st.dataframe(df)

with tab2:
	st.write(df.describe())

with tab3:
	st.write(df.shape)
