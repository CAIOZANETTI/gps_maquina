import streamlit as st
import pandas as pd
import fx_streamlit as fx_streamlit

st.header("Extração BRONZE")

files = [
	#'data/silver_jcb_relatorio_2022.parquet',
	'data/bronze_jcb_relatorio_2022.parquet',
	]

st.selectbox('files',files,key='file')	
#uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)

try:
	df = pd.read_parquet(st.session_state['file'],engine='pyarrow')
except:
	df = pd.read_parquet(st.session_state['file'],engine='fastparquet')

fx_streamlit.analise_df(df,'bronze ....')

st.session_state['df'] = df
st.write('teste')