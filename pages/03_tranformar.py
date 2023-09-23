import streamlit as st
import pandas as pd
import math

import fx_streamlit as fx_streamlit
import fx_data as fx_data


# carregar ou ler silver
if 'df1' not in st.session_state:
	df1 = pd.read_parquet('data/silver_jcb_relatorio_2022.parquet',engine='pyarrow')
else:
	df = pd.read_parquet('data/bronze_jcb_relatorio_2022.parquet',engine='pyarrow')
	remover_colunas = ['id','hyperlink','maps_google_url']
	df1 = fx_data.df_bronze_to_silver_gps(df=df,remover_colunas=remover_colunas)
st.session_state['df1'] = df1

# carregar ou download silver
btn_reload = st.button('recarregar')
if btn_reload == True:
	df = pd.read_parquet('data/bronze_jcb_relatorio_2022.parquet',engine='pyarrow')
	remover_colunas = ['id','hyperlink','maps_google_url']
	df1 = fx_data.df_bronze_to_silver_gps(df=df,remover_colunas=remover_colunas)
	st.session_state['df1'] = df1

#mostrar analise
fx_streamlit.analise_df(df1,'silver....')

#teste
st.write('some info')