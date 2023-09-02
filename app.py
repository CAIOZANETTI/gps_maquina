import datetime
import streamlit as st
import pandas as pd

#modulos
import listas as lst
import extrair
import caminhos

hoje={}
hoje['datetime'] = datetime.datetime.now()
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

with st.expander('raw',expanded=True):
	df = extrair.gsheet_to_df(
		id = caminho['id'],
		tabela=caminho['tabela'],
		testar=False)
	st.dataframe(df)

with st.expander('bronze',expanded=False):
	def df_bronze(coluna:str,df)->pd.DataFrame:
		df[['data','horas']] = df[coluna].str.split(' ', expand=True)

		df[['dia','mes','ano']] = df['data'].str.split('/', expand=True)
		df['dia'] = df['dia'].astype(int)
		df['mes'] = df['mes'].astype(int)
		df['ano'] = df['ano'].astype(int)

		df[['hora','minuto']] = df['horas'].str.split(':', expand=True)
		df['hora'] = df['hora'].astype(int)
		df['minuto'] = df['minuto'].astype(int)

		df['coordenadas'] = df['maps_google_url'].str.replace("http://maps.google.com/?q=", "")
		df['lat'] = df['coordenadas'].str.slice(2, 15)
		df['lon'] = df['coordenadas'].str.slice(15, 25)

		return df

	df1 = df_bronze(coluna='data_hora',df=df)
	st.dataframe(df1)

with st.expander('silver',expanded=False):
	st.dataframe(df)

with st.expander('gold',expanded=False):
	st.dataframe(df)