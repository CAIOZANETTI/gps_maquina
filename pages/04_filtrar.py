import datetime
import streamlit as st
import pandas as pd
#from datetime import datetime

import fx_streamlit as fx_streamlit

def df_filtrar_datas(df:pd.DataFrame,inicio,fim)->pd.DataFrame:
	df['data'] = df['data_hora'].dt.date
	df1 = df[(df['data']>= inicio) & (df['data']<= fim)]
	return df1

st.subheader("Filtrar")
if 'df1' not in st.session_state:
	df1 = pd.DataFrame()
	st.write('df1 esta vazio!!! voltar e transformar')

df1 = st.session_state['df1']
tab1,tab2,tab3 = st.tabs(['periodo','atividades','dia da semana'])

with tab1: #periodo
	st.text('disponivel: jan/2022 -> ago/2022')
	cols = st.columns([1,1])
	cols[0].date_input('inicio',datetime.datetime(2022,1,1),key='inicio')
	cols[1].date_input('fim',datetime.datetime(2022,1,8),key='fim')

	dias = st.session_state['fim'] - st.session_state['inicio']
	dias = dias.days

	if dias>0:
		cols = st.columns([1,1])
		cols[0].write('Periodo: '+str(dias)+' dias')
		desativo=False

	elif dias<0:
		cols[0].write('NEGATIVO REVISAR '+str(dias)+' dias')
		desativo=True

with tab2: #atividades
	atividades = df1['atividade'].unique()
	st.multiselect('atividades',atividades,default=atividades,key='atividades')	

with tab3: #dia da semana
	dias = df1['nome_dia'].unique()
	st.multiselect('dia semana',dias,default=dias,key='nome_dia')
	

st.button('filtrar dataframe',key='filtrar_dataframe',disabled=desativo,type='primary')
df2 = df1
if st.session_state['filtrar_dataframe']==True:
	df2 = df_filtrar_datas(df2,inicio=st.session_state['inicio'],fim = st.session_state['fim'])
	df2 = df2[df2['atividade'].isin(st.session_state['atividades'])]
	df2 = df2[df2['nome_dia'].isin(st.session_state['nome_dia'])]

fx_streamlit.analise_df(df2,'silver filtrado')

st.divider()
st.subheader("Filtro Aplicado Dataframe")
tab1,tab2,tab3 = st.tabs(['dataframe','mapa','grafico'])

with tab1:#dataframe
	st.dataframe(df2)

with tab2:#mapa
	df_map = df2[['lat','lon']]
	#df_map['cor'] = "#001eff"
	#df_map['raio'] = 5
	st.map(df_map, latitude='lat',longitude='lon')#,size='raio',color='cor')

with tab3:#grafico
	st.write('ocorrencias')


st.subheader("Cronologia, linha do tempo...")
st.subheader("Relação entre variaveis")