import datetime
import pytz

import streamlit as st
import pandas as pd

#modulos
import listas as lst
import extrair
import caminhos
import funcoes_gps
import filtros

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
	st.text("pytz.timezone('America/Sao_Paulo')")
	cols[0].text(hoje['data'])
	cols[1].text(hoje['hora'])
	
   
	#usuario 	
	#st.selectbox("usuarios",lst.usuarios,key='usuario')
	#st.write(st.session_state['usuario'])
	st.radio("relatorios",['filtros','calculos','futuro'],key='relatorios')

with st.expander("df dataframe completo linhas:"+str(df.shape[0]), expanded=False):
	st.dataframe(df)

if st.session_state['relatorios']== 'filtros':
	with st.expander("filtrar dataframe", expanded=True):
			
		cols = st.columns([1,1,1,1])
		cols[0].text('periodo disponivel')
		cols[0].text('jan/2022 -> ago/2022')
		cols[1].date_input('inicio',datetime.datetime(2022,1,1),key='inicio')
		cols[2].date_input('fim',datetime.datetime(2022,1,8),key='fim')

		cols[3].text('ativar')
		cols[3].button('filtros',key='btn_filtrar')
		
		if st.session_state['btn_filtrar']:
			df1 = filtros.df_periodo(df,st.session_state['inicio'],st.session_state['fim'])
		
			with st.expander("**df1** dataframe filtrado linhas:"+str(df.shape[0]), expanded=False):
				st.dataframe(df1)

			with st.expander('mapa', expanded=False):
				st.write('mapas')
				df2 = df1[['lat','lon']]
				st.map(df2)

			with st.expander('tabelas', expanded=False):
				st.write('tabelas')

			with st.expander('graficos', expanded=False):
				st.write('graficos')