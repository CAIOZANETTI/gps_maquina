import datetime
import streamlit as st
import pandas as pd
#from datetime import datetime


def df_filtrar_datas(df:pd.DataFrame,inicio,fim)->pd.DataFrame:
	df['data'] = df['data_hora'].dt.date
	df1 = df[(df['data']>= inicio) & (df['data']<= fim)]
	return df1

st.subheader("Filtrar")
df1 = st.session_state['df1']
tab1,tab2,tab3,tab4 = st.tabs(['periodo','atividades principais','todas atividades','3-dia da semana'])

with tab1:
	st.text('disponivel: jan/2022 -> ago/2022')
	cols = st.columns([1,1])
	cols[0].date_input('inicio',datetime.datetime(2022,1,1),key='inicio')
	cols[1].date_input('fim',datetime.datetime(2022,1,8),key='fim')

	dias = st.session_state['fim'] - st.session_state['inicio']
	dias = dias.days


	if dias>0:
		cols = st.columns([1,1])
		st.write('Periodo: '+str(dias)+' dias')
		st.button('filtrar_datas',key=filtrar_datas)

	elif dias<0:
		st.write('NEGATIVO REVISAR '+str(dias)+' dias')

	df2 = df1
	if st.session_state['filtrar_datas']==True:
		df2 = df_filtrar_datas(df1,
			inicio=st.session_state['inicio'],
			fim = st.session_state['fim'])

with tab2:
	st.write('atividades principais')

with tab3:
	st.write('todas atividades')

with tab4:
	st.write('dia da semana')

st.divider()
st.subheader("Filtro Aplicado Dataframe")
tab1,tab2,tab3 = st.tabs(['dataframe','mapa','dias'])

with tab1:
	st.dataframe(df2)

with tab2:
	df_map = df1[['lat','lon']]
	df_map['cor'] = "#001eff"
	df_map['raio'] = 5
	st.map(df_map, latitude='lat',longitude='lon',size='raio',color='cor')


with tab3:
	st.write('todas atividades')