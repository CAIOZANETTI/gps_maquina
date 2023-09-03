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

abas = ['raw','bronze','silver','gold']
st.selectbox('expandir',abas,key='ver')


with st.expander('raw',expanded=False):
	df = extrair.gsheet_to_df(
		id = caminho['id'],
		tabela=caminho['tabela'],
		testar=False)
	st.dataframe(df)

st.write(df['atividade'].unique())

with st.expander('bronze',expanded=False):
	def df_bronze(coluna:str,col_remover:list,df)->pd.DataFrame:
		"""
		converter: data, hora e latitude e longitude
		"""

		df[['data','horas']] = df[coluna].str.split(' ', expand=True)

		df[['dia','mes','ano']] = df['data'].str.split('/', expand=True)
		df['dia'] = df['dia'].astype(int)
		df['mes'] = df['mes'].astype(int)
		df['ano'] = df['ano'].astype(int)

		df[['hora','minuto']] = df['horas'].str.split(':', expand=True)
		df['hora'] = df['hora'].astype(int)
		df['minuto'] = df['minuto'].astype(int)

		df['lat1'], df['lon1'] = zip(*df['maps_google_url'].apply(funcoes_gps.url_to_coordenadas))
		
		df['lat2'] = df['lat1'].shift(-1)
		df['lon2'] = df['lon1'].shift(-1)


		for coluna in col_remover:
			if coluna in df.columns:
				df = df.drop(coluna,axis=1)

		return df

	col_remover = ['id','data_hora','hyperlink','maps_google_url']
	df1 = df_bronze(coluna='data_hora',df=df,col_remover=col_remover)
	st.write(df_bronze.__doc__)
	st.dataframe(df1.head(5))

with st.expander('silver',expanded=True):
	def df_silver(df)-pd.DataFrame:
		"""
		Calcular distancia percorrida
	
		"""
		df['lat_dist'] = df['lat1']-df['lat2']

		return df

	df2 = df_silver(df=df1)
	st.dataframe(df2)

with st.expander('gold',expanded=False):
	st.dataframe(df)