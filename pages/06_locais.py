import streamlit as st
import pandas as pd


import extrair as extrair
import fx_streamlit as fx_streamlit


if 'df1' not in st.session_state:
	df1 = pd.read_parquet('data/silver_jcb_relatorio_2022.parquet',engine='pyarrow')
	st.session_state['df1'] = df1
df1 = st.session_state['df1']

st.subheader('Mapa de Localização')

with st.expander('localização com maior incidencia', expanded=True):
	
	df_map = df1[['lat','lon']].describe()
	df_map = df_map.reset_index()
	
	df_map_relev = df_map.query('index=="50%" and index=="75%" and index=="max"')
	st.dataframe(df_map_relev)



	#st.write(df_map[''.loc['75%'])
	#st.write(df_map.loc['max'].T)
	st.map(df_map_relev)


