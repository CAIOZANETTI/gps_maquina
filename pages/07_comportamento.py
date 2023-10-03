import streamlit as st
import pandas as pd


if 'df1' not in st.session_state:
	df1 = pd.read_parquet('data/silver_jcb_relatorio_2022.parquet',engine='pyarrow')
	st.session_state['df1'] = df1

df1 = st.session_state['df1']

tab1,tab2,tab3,tab4,tab5 = st.tabs(['dia semana','horas','inicio','\
	','domingo'])

filtro = 'motor_ligado==True'
st.write('Produtiva: '+filtro)
df2 = df1.query(filtro)
with tab1: 	
	st.dataframe(df2['nome_dia'].value_counts())
with tab2:
	st.dataframe(df2['hora'].value_counts().sort_index())
with tab3:
	st.write('primeira hora que a chave ligou')
	inicio = df1[df1['atividade'] == 'chave_ligada']['hora'].iloc[0]
	st.dataframe(inicio)

with tab4:
with tab5:


filtro = 'motor_ligado==False'
st.write('Improdutiva: '+filtro)
df2 = df1.query(filtro)
