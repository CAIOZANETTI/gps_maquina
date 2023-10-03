import streamlit as st
import pandas as pd


if 'df1' not in st.session_state:
	df1 = pd.read_parquet('data/silver_jcb_relatorio_2022.parquet',engine='pyarrow')
	st.session_state['df1'] = df1

df1 = st.session_state['df1']

with st.expander('info',expanded=False):
	st.markdown('analisar a rotina da maqiona no periodo disponivel no dataframe,\
	 afim de identificar algum padrão que possa ser caracterizado como um comportamento')

tab1,tab2,tab3,tab4,tab5 = st.tabs(['dias','horas','inicio','termino'])

filtro = 'motor_ligado==True'
st.write('Produtiva: '+filtro)
df2 = df1.query(filtro)
with tab1:
 	st.write('segunda -> sexta')
 	st.write('sabado')
 	st.write('domingo')
	st.dataframe(df2['nome_dia'].value_counts())

with tab2:
	st.write('dia')
	st.write('noite')
	st.write('madrugada')

	st.dataframe(df2['hora'].value_counts().sort_index())
with tab3:
	st.write('primeira hora do dia que a chave ligou')
	inicio = df1[df1['atividade'] == 'chave_ligada']['hora'].iloc[0]
	st.dataframe(inicio)

with tab4:
	st.write('ultima hora hora do dia que a chave desligou')



filtro = 'motor_ligado==False'
st.write('Improdutiva: '+filtro)
df2 = df1.query(filtro)
