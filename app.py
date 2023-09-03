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

with st.sidebar:
	cols = st.columns([1,1])
	cols[0].text(hoje['data'])
	cols[1].text(hoje['hora'])
	
	with st.expander('usuario',expanded=True):
		st.selectbox("usuarios",lst.usuarios,key='usuario')
		st.write(st.session_state['usuario'])

caminho =caminhos.tabelas['jcb_relatorio'] 
#st.write(caminho)

st.write('transformação da tabela')

with st.expander('testar funcoes',expanded=True):
	lst= [
	'("http://maps.google.com/?q=-26,6066705,-51,0989749","Calmon (Calmon)")',
	'("http://maps.google.com/?q=-26,6069566,-51,0962178","-26,6069566,-51,0962178")',
	'("http://maps.google.com/?q=-26,607,-51,0961821","-26,607,-51,0961821")',
	'("http://maps.google.com/?q=-26,6026343,-51,102305","-26,6026343,-51,102305")',
	'("http://maps.google.com/?q=-26,606305,-51,0996484","-26,606305,-51,0996484")',
	]

	for url in lst:
		teste = funcoes_gps.url_to_coordenadas(url)
		st.write(teste)



with st.expander('raw',expanded=True):
	df = extrair.gsheet_to_df(
		id = caminho['id'],
		tabela=caminho['tabela'],
		testar=False)
	st.dataframe(df)

with st.expander('bronze',expanded=False):
	def df_bronze(coluna:str,col_remover:list,df)->pd.DataFrame:
		"""

		"""
		df[['data','horas']] = df[coluna].str.split(' ', expand=True)

		df[['dia','mes','ano']] = df['data'].str.split('/', expand=True)
		df['dia'] = df['dia'].astype(int)
		df['mes'] = df['mes'].astype(int)
		df['ano'] = df['ano'].astype(int)

		df[['hora','minuto']] = df['horas'].str.split(':', expand=True)
		df['hora'] = df['hora'].astype(int)
		df['minuto'] = df['minuto'].astype(int)

		df['lat'], df['lon'] = zip(*df['maps_google_url'].apply(funcoes_gps.url_to_coordenadas))
		
		for coluna in col_remover:
			if coluna in df.columns:
				df = df.drop(coluna,axis=1)

		return df

	col_remover = ['data_hora','hyperlink','maps_google_url']
	df1 = df_bronze(coluna='data_hora',df=df,col_remover=col_remover)
	st.dataframe(df1)

with st.expander('silver',expanded=False):
	st.dataframe(df)

with st.expander('gold',expanded=False):
	st.dataframe(df)