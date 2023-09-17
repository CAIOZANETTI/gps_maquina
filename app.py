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

# carregar variaveis do json
dic = extrair.json_to_dic('variaveis.json')
df_locais = pd.DataFrame(dic['locais'])

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

with st.expander("locais conhecidos", expanded=False):
	#df_locais = pd.DataFrame(dic['locais'])
	st.write(df_locais)

with st.expander("df dataframe completo linhas:"+str(df.shape[0]), expanded=False):
	st.dataframe(df)

if st.session_state['relatorios']== 'filtros':
	with st.expander("filtrar dataframe", expanded=True):

		#periodo
		st.text('disponivel: jan/2022 -> ago/2022')
		cols = st.columns([1,1])
		cols[0].date_input('inicio',datetime.datetime(2022,1,1),key='inicio')
		cols[1].date_input('fim',datetime.datetime(2022,1,8),key='fim')

		#st.date_input('perido',datetime.datetime(2022,1,8),datetime.datetime(2022,1,8),key='inicio_fim')
		#st.write(st.session_state['inicio_fim'])		

		#atividade
		atividades = df['atividade'].unique()
		st.multiselect('atividades',atividades,default=atividades,key='atividades')

		#dia da semana
		dias = df['nome_dia'].unique()
		st.multiselect('dia semana',dias,default=dias,key='nome_dia')		

		#controle
		cols = st.columns([1,1])
		cols[0].text('ativar')
		cols[1].button('filtros',key='btn_filtrar')
		
		if st.session_state['btn_filtrar']:
			df1 = filtros.df_periodo(df,inicio=st.session_state['inicio'],fim=st.session_state['fim'])
			df1 = df1[df['atividade'].isin(st.session_state['atividades'])]
			df1 = df1[df['nome_dia'].isin(st.session_state['nome_dia'])]
			
			st.dataframe(df1)
			st.write('mapas')

			df2 = df1[['lat','lon']]
			df2['nome'] = df1['atividade']
			df2['cor'] = "#001eff"
			df2['raio'] = 5

			st.write(df2)
			st.write(df_locais)
			df_map = pd.concat([df2,df_locais],ignore_index=True)
			st.write(df_map)

			#st.map(df2, latitude='lat',longitude='lon',size='raio',color='cor')
			#st.map(df_locais, latitude='lat',longitude='lon',size='raio',color='cor')	

			#df_map = pd.concat([df2,df_locais],ignore_index=True)		
			#st.map(df_map, latitude='lat',longitude='lon',size='raio',color='cor')