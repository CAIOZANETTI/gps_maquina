import streamlit as st
import pandas as pd

st.header("escolher arquivo formato parquet para primeira extração BRONZE")


files = [
	#'data/silver_jcb_relatorio_2022.parquet',
	'data/bronze_jcb_relatorio_2022.parquet',
	]

st.selectbox('files',files,key='file')	
#uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)

tab1,tab2,tab3,tab4,tab5 = st.tabs(['dataframe','describe','shape','columns','bytes'])

try:
	df = pd.read_parquet(st.session_state['file'],engine='pyarrow')
except:
	df = pd.read_parquet(st.session_state['file'],engine='fastparquet')

with tab1:
	st.dataframe(df)

with tab2:
	st.write(df.describe())

with tab3:
	shape = {}
	shape['rows'] = df.shape[0]
	shape['columns'] = df.shape[1]
	st.write(shape)

with tab4:
	st.write(df.columns)

with tab5:
	memory = {}
	memory['bytes'] = int(df.memory_usage(deep=True).sum())
	memory['Kb'] = round(memory['bytes'] / 1024,2)
	memory['Mb'] = round(memory['bytes'] / 1048576,2)
	
	st.write(memory)

st.session_state['df'] = df