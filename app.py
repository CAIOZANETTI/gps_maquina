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

# ler dataframe
files = [
	'data/silver_jcb_relatorio_2022.parquet',
	'data/bronze_jcb_relatorio_2022.parquet',
	]

try:
	df = pd.read_parquet(files[0],engine='pyarrow')
except:
	df = pd.read_parquet(files[0],engine='fastparquet')


with st.sidebar:
	#data
	cols = st.columns([1,1])
	cols[0].text(hoje['data'])
	cols[1].text(hoje['hora'])
	
	#df shape
	cols = st.columns([1,1,1])
	cols[0].write('df')
	cols[1].write('lin: '+str(df.shape[0]))
	cols[2].write('col: '+str(df.shape[1]))
   
	#usuario 	
	#st.selectbox("usuarios",lst.usuarios,key='usuario')
	#st.write(st.session_state['usuario'])
	st.radio("relatorios",['mapas','tabelas','graficos'],key='relatorios')

with st.expander("dataframe", expanded=False):
	st.dataframe(df)    

if st.session_state['relatorios']== 'mapas':
	st.write('mapas')
	df2 = df[['lat','lon']]
	st.map(df2)
if st.session_state['relatorios']== 'tabelas':
	st.write('tabelas')

if st.session_state['relatorios']== 'graficos':
	st.write('graficos')