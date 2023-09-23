import streamlit as st
import pandas as pd


if 'df1' not in st.session_state:
	df1 = pd.read_parquet('data/silver_jcb_relatorio_2022.parquet',engine='pyarrow')
	st.session_state['df1'] = df1

df1 = st.session_state['df1']

with st.sidebar:
	idioma = st.radio('idioma dos comentarios', ['portugues','ingles'])

st.subheader("Entendimento")

st.write(
'A compreender as informações dos dados\
identificar quais informações são relevantes,\
como elas estão distribuídas, qual a relação\
entre demais variáveis como o tempo (hora, dia, mês)\
ou coordenadas lat+lon.')

# atividades....
st.subheader('atividades')
tab1,tab2,tab3,tab4 = st.tabs(['contagem','horimetro','horas','dia da semana'])

with tab1: #contagem

	if idioma=='portugues': 
		st.text('Realizar uma análise da coluna de atividades por meio de um filtro para identificar aquelas que são mais frequentes e relevante')
	if idioma=='ingles':
		st.text('Perform an analysis of the activities column through a filter to identify the most frequent and relevant ones')

	df2 = df1['atividade'].value_counts().reset_index()
	df2.columns = ['atividade','qtd']
	df2['perc'] = round(100*(df2['qtd']/df2['qtd'].sum()),0)
	df2['perc'] = df2['perc'].astype(int)
	df2['util'] = df2['perc']>5


	st.dataframe(df2)


with tab2: #periodo

	st.write('atividades vs horas')
	pivot_df = df1.pivot_table(index='hora', columns='atividade', aggfunc='size', fill_value=0)
	df3 = pivot_df.T.reset_index()

	st.dataframe(df3.head(5))

	pivot_df = df1.pivot_table(index='atividade', columns='hora', aggfunc='size', fill_value=0)

	st.dataframe(pivot_df)
	#st.bar_chart(df1[['atividade','hora']])

with tab3: #periodo
	st.write(' atividades vs dia da semana')


with tab4: #periodo
	st.write(' atividades vs dia da semana')


st.write('interpretação')
st.write('para determinar a ')