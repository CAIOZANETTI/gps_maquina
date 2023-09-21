import streamlit as st
import pandas as pd


st.subheader("Entendimento")

st.write(
'A compreender as informações dos dados\
identificar quais informações são relevantes,\
como elas estão distribuídas, qual a relação\
entre demais variáveis como o tempo (hora, dia, mês)\
ou coordenadas lat+lon.')

# atividades....
#tab1,tab2,tab3,tab4 = st.tabs(['atividade_unicas','dias'])

if 'df1' not in st.session_state:
	df1 = pd.DataFrame()
	st.write('df1 esta vazio!!! voltar e transformar')

df1 = st.session_state['df1']





tab1,tab2,tab3 = st.tabs(['atividades','atividades vs horas',' atividades vs dia da semana'])

with tab1: #periodo
	df2 = df1['atividade'].value_counts().reset_index()
	df2.columns = ['atividade','qtd']
	qtd_min = int(round(df2['qtd'].min(),0))
	qtd_max = int(round(df2['qtd'].max(),0))
	qtd_total = df2['qtd'].sum()
	
	#df2['perc']=round((df2['qtd']/qtd_total)*100,2)


	st.data_editor(
	    df2,
	    column_config={
	        "qtd": st.column_config.ProgressColumn(
	      
	            width='large',
	            format='%f',
	            min_value=qtd_min,
	            max_value=qtd_max,
	        ),
	    },
	    hide_index=True,
	)



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