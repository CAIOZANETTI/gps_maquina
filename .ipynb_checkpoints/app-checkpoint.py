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


relatorios = ['mapa','tabelas','graficos']
with st.sidebar:
    cols = st.columns([1,1])
	cols[0].text(hoje['data'])
	cols[1].text(hoje['hora'])
	
	st.selectbox("usuarios",lst.usuarios,key='usuario')
    st.write(st.session_state['usuario'])
    st.selectbox("relatorios",relatorios,key='relatorio')
    
    

caminho =caminhos.tabelas['jcb_relatorio_2022'] 
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

cols = st.columns([1,1])
cols[0].write(df.describe())
cols[1].write(df['atividade'].value_counts())

with st.expander('bronze',expanded=False):
	def df_bronze(coluna:str,col_remover:list,df)->pd.DataFrame:
		"""
		converter: data, hora e latitude e longitude
		"""
		
		df['data_hora'] = pd.to_datetime(df['data_hora'], format='%m/%d/%Y %H:%M:%S')

		#df[['data','horas1']] = df[coluna].str.split(' ', expand=True)

		#df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
		#df['houras1'] = pd.to_datetime(df['horas1'], format='%H:%M').dt.time

		# não vou detalhar, foicou confuso
		#df[['dia','mes','ano']] = df['data'].str.split('/', expand=True)
		#df['dia'] = df['dia'].astype(int)
		#df['mes'] = df['mes'].astype(int)
		#df['ano'] = df['ano'].astype(int)

		#df[['hora','minuto']] = df['horas'].str.split(':', expand=True)
		#df['hora'] = df['hora'].astype(int)
		#df['minuto'] = df['minuto'].astype(int)

		df['lat1'], df['lon1'] = zip(*df['maps_google_url'].apply(funcoes_gps.url_to_coordenadas))
		
		for coluna in col_remover:
			if coluna in df.columns:
				df = df.drop(coluna,axis=1)

		return df

	col_remover = ['id','hyperlink','maps_google_url']
	df1 = df_bronze(coluna='data_hora',df=df,col_remover=col_remover)
	st.write(df_bronze.__doc__)
	st.dataframe(df1.head(5))

with st.expander('silver',expanded=True):


	st.selectbox('atividades',df1['atividade'].unique(),key='atividade')


	def df_silver(df)->pd.DataFrame:
		"""
		incluir linha anterior (lat0, long0, data_hora0)
		calcular: raio, minutos, velocidade
		*raio metros (não leva en consideração as ruas)

		"""
		def kmph(metros,minutos):
			velocidade=0
			if metros >0 and minutos>0:
				velocidade = round((metros/minutos)*(60/1000),2)
			return velocidade

		df['lat0'] = df['lat1'].shift(+1)
		df['lon0'] = df['lon1'].shift(+1)
		df['data_hora0'] = df['data_hora'].shift(+1)

		df['raio_m'] = df.apply(lambda row: funcoes_gps.haversine_distance(row['lat0'], row['lon0'], row['lat1'], row['lon1']), axis=1)
		df['minutos'] = (df['data_hora'] - df['data_hora0']).dt.total_seconds() / 60
		

		df['kmph'] =df.apply(lambda row: kmph(row['raio_m'], row['minutos']), axis=1)
		df['kmph'].fillna(0, inplace=True)

		return df

	df2 = df_silver(df=df1)
	st.write(df_silver.__doc__)
	st.dataframe(df2)

with st.expander('gold',expanded=False):
	def df_gold(df)->pd.DataFrame:
		"""
		entender premisass das atividades confirmar com jcb:
		(talvez seja o gps pq isso ocorre de madrugada)  
		Ligado, Estado Activo, Primeiro Acerto do GPS, Prestes a Entrar em Estado de Descanso

		filtrar ocorrencias significativas
	
		"""
		pass




	st.dataframe(df)