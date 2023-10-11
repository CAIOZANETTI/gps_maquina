import streamlit as st
import pandas as pd

import fx_streamlit as fx_streamlit



if 'df1' not in st.session_state:
	df1 = pd.read_parquet('data/silver_jcb_relatorio_2022.parquet',engine='pyarrow')
	st.session_state['df1'] = df1

df1 = st.session_state['df1']

st.subheader('Analise **Comportamentos** atividade, periodos localização')

tab1,tab2,tab3,tab4,tab5 = st.tabs(['improvavel','madrugada','manhã','tarde','noite'])


with tab1:
	
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
		st.map(df2[['lat','lon']])

	with st.expander('informação do dataframe', expanded=False):
		fx_streamlit.analise_df(df2,filtro_ativo)

with tab2:
	filtro = [
		'(hora>0) and (hora<6)',
		'(motor_ligado==True) and (hora>0) and (hora<6)'
		]
	filtro_ativo = st.selectbox('filtrar as condições:',filtro)

	with st.expander('dataframe', expanded=False):
		df2 = df1.query(filtro_ativo)
		st.dataframe(df2)

	with st.expander('Mapa', expanded=True):
		st.map(df2[['lat','lon']])

	with st.expander('informação do dataframe', expanded=False):
		fx_streamlit.analise_df(df2,filtro_ativo)

with tab3:
	filtro = [
		'(hora>6) and (hora<12)',
		'(motor_ligado==True) and (hora>6) and (hora<12)'
		]
	filtro_ativo = st.selectbox('filtrar as condições:',filtro)

	with st.expander('dataframe', expanded=False):
		df2 = df1.query(filtro_ativo)
		st.dataframe(df2)

	with st.expander('Mapa', expanded=True):
		st.map(df2[['lat','lon']])
	
	with st.expander('informação do dataframe', expanded=False):
		fx_streamlit.analise_df(df2,filtro_ativo)

with tab4:
	filtro = [
		'(hora>12) and (hora<18)',
		'(motor_ligado==True) and (hora>12) and (hora<18)'
		]
	filtro_ativo = st.selectbox('filtrar as condições:',filtro)

	with st.expander('dataframe', expanded=False):
		df2 = df1.query(filtro_ativo)
		st.dataframe(df2)

	with st.expander('Mapa', expanded=True):
		st.map(df2[['lat','lon']])

	with st.expander('informação do dataframe', expanded=False):
		fx_streamlit.analise_df(df2,filtro_ativo)

with tab5:
	filtro = [
		'(hora>18)',
		'(motor_ligado==True) and (hora>18)'
		]
	filtro_ativo = st.selectbox('filtrar as condições:',filtro)

	with st.expander('dataframe', expanded=False):
		df2 = df1.query(filtro_ativo)
		st.dataframe(df2)

	with st.expander('Mapa', expanded=True):
		st.map(df2[['lat','lon']])

	with st.expander('informação do dataframe', expanded=False):
		fx_streamlit.analise_df(df2,filtro_ativo)

