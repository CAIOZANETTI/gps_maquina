import streamlit as st
import pandas as pd

import fx_streamlit as fx_streamlit



if 'df1' not in st.session_state:
	df1 = pd.read_parquet('data/silver_jcb_relatorio_2022.parquet',engine='pyarrow')
	st.session_state['df1'] = df1

df1 = st.session_state['df1']

st.subheader('Analise **Comportamentos** atividade, periodos e localização')

#cols = st.columns(['1,1'])
ano_mes_unico = df1['ano_mes'].unique()
st.selectbox('selcionar ano mes',ano_mes_unico,key='ano_mes')
df1 = df1[df1['ano_mes'] ==st.session_state['ano_mes']]

tab1,tab2,tab3,tab4,tab5 = st.tabs(['manhã','tarde','noite','madrugada','improvavel'])

with tab1:
	filtro = [
		'(hora>6) and (hora<12)',
		'(motor_ligado==True) and (hora>6) and (hora<12)'
		]
	filtro_ativo = st.selectbox('filtrar as condições:',filtro)

	with st.expander('dataframe', expanded=False):
		df2 = df1.query(filtro_ativo)
		st.dataframe(df2)

	with st.expander('Mapa', expanded=True):
		st.map(df2[['lat','lon']],size=5)
	
	with st.expander('informação do dataframe', expanded=False):
		fx_streamlit.analise_df(df2,filtro_ativo)

with tab2:
	filtro = [
		'(hora>12) and (hora<18)',
		'(motor_ligado==True) and (hora>12) and (hora<18)'
		]
	filtro_ativo = st.selectbox('filtrar as condições:',filtro)

	with st.expander('dataframe', expanded=False):
		df2 = df1.query(filtro_ativo)
		st.dataframe(df2)

	with st.expander('Mapa', expanded=True):
		st.map(df2[['lat','lon']],size=5)

	with st.expander('informação do dataframe', expanded=False):
		fx_streamlit.analise_df(df2,filtro_ativo)

with tab3:
	filtro = [
		'(hora>18)',
		'(motor_ligado==True) and (hora>18)'
		]
	filtro_ativo = st.selectbox('filtrar as condições:',filtro)

	with st.expander('dataframe', expanded=False):
		df2 = df1.query(filtro_ativo)
		st.dataframe(df2)

	with st.expander('Mapa', expanded=True):
		st.map(df2[['lat','lon']],size=5)

	with st.expander('informação do dataframe', expanded=False):
		fx_streamlit.analise_df(df2,filtro_ativo)

with tab4:
	filtro = [
		'(hora>0) and (hora<6)',
		'(motor_ligado==True) and (hora>0) and (hora<6)'
		]
	filtro_ativo = st.selectbox('filtrar as condições:',filtro)

	with st.expander('dataframe', expanded=False):
		df2 = df1.query(filtro_ativo)
		st.dataframe(df2)

	with st.expander('Mapa', expanded=True):
		st.map(df2[['lat','lon']],size=5)

	with st.expander('informação do dataframe', expanded=False):
		fx_streamlit.analise_df(df2,filtro_ativo)

with tab5:
	with st.expander('motor foi ligado em dia de **folga**', expanded=True):
		filtro = [
		'(motor_ligado==True) and (nome_dia=="sunday")',
		'(motor_ligado==True) and (nome_dia=="saturday")and (hora>13)',
		]
		filtro_ativo = st.selectbox('filtrar as condições:',filtro)

	with st.expander('dataframe', expanded=False):
		df2 = df1.query(filtro_ativo)
		st.dataframe(df2)

	with st.expander('Mapa', expanded=True):
		st.map(df2[['lat','lon']],size=5)

	with st.expander('informação do dataframe', expanded=False):
		fx_streamlit.analise_df(df2,filtro_ativo)