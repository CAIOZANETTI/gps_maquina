import streamlit as st
import pandas as pd
import fx_streamlit as fx_streamlit

st.header("Extração RAW->BRONZE")

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

with st.expander('info',expanded=False):
	st.write('Primeira extração dos dados de como foi disponibilizado,\
		sem nenhuma modificação os dados estão em formato original (RAW),\
		essa primeira etapa apenas tranforma em formato dataframe pandas\
		o resultado pode ser verificado nas abas de info sobre o dataframe')

fx_streamlit.analise_df(df,'raw-> bronze')
st.session_state['df'] = df
