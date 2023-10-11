import streamlit as st
import pandas as pd
import math

import extrair as extrair
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

#textos e idioma
textos = extrair.json_to_dic('textos.json')
cols = st.columns([1,1])
idioma = cols[0].radio('idioma dos comentarios', ['portugues','ingles'])
textos = textos['03_transformar'][idioma]


# carregar ou download silver
btn_reload = st.button('recarregar')

with st.expander('info',expanded=False):
	st.markdown(textos['tempo'])
	st.markdown(textos['local'])
	st.markdown(textos['atividade'])

if btn_reload == True:
	df = pd.read_parquet('data/bronze_jcb_relatorio_2022.parquet',engine='pyarrow')
	remover_colunas = ['id','hyperlink','maps_google_url']
	df1 = fx_data.df_bronze_to_silver_gps(df=df,remover_colunas=remover_colunas)
	st.session_state['df1'] = df1

#mostrar analise
fx_streamlit.analise_df(df1,'bronze->silver')

#teste
st.write('some info')