import datetime
import pytz

import streamlit as st
import pandas as pd

#modulos
import listas as lst
import extrair
import caminhos
import funcoes_gps


brazil_tz = pytz.timezone('America/Sao_Paulo')
hoje={}
hoje['datetime'] = datetime.datetime.now(brazil_tz)
hoje['data'] = hoje['datetime'].date()
hoje['hora'] = hoje['datetime'].time()

file = 'https://github.com/CAIOZANETTI/produtividade_maquina/blob/main/data/bronze_jcb_relatorio_2022.parquet'
try:
	df = pd.read_parquet(file,engine='pyarrow')

except:
	df = pd.read_parquet(file,engine='fastparquet')


with st.sidebar:
	cols = st.columns([1,1])
	cols[0].text(hoje['data'])
	cols[1].text(hoje['hora'])

	st.write(df.shape[0])
   #display('df from:'+file)
   #st.selectbox("usuarios",lst.usuarios,key='dataframe')
	
	#st.selectbox("usuarios",lst.usuarios,key='usuario')
	#st.write(st.session_state['usuario'])

	st.radio("relatorios",['mapas','tabelas','graficos'],key='relatorios')

	st.write('dataframe')




    

if st.session_state['relatorios']== 'mapas':
	st.write('mapas')

if st.session_state['relatorios']== 'tabelas':
	st.write('tabelas')

if st.session_state['relatorios']== 'graficos':
	st.write('graficos')