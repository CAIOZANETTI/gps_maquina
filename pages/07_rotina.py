import streamlit as st
import pandas as pd


if 'df1' not in st.session_state:
	df1 = pd.read_parquet('data/silver_jcb_relatorio_2022.parquet',engine='pyarrow')
	st.session_state['df1'] = df1

df1 = st.session_state['df1']

with st.expander('info',expanded=False):
	st.markdown('analisar a rotina da maqiona no periodo disponivel no dataframe,\
	 afim de identificar algum padrão que possa ser caracterizado como um comportamento')

tab1,tab2,tab3,tab4,tab5 = st.tabs(['semana','horas','deslocamento','inicio','termino'])


with tab1:

	cols = st.columns([1,1,1,1,1])
	filtro = 'motor_ligado==True'
	cols[0].write(filtro)
	df2 = df1.query(filtro)
	cols[0].dataframe(df2['nome_dia'].value_counts())
	
	filtro = 'motor_ligado==False'
	cols[1].write(filtro)
	df2 = df1.query(filtro)
	cols[1].dataframe(df2['nome_dia'].value_counts())

	filtro = 'atividade=="chave_ligada"'
	cols[2].write(filtro)
	df2 = df1.query(filtro)
	cols[2].dataframe(df2['nome_dia'].value_counts())
	
	filtro = 'atividade=="chave_desligada"'
	cols[3].write(filtro)
	df2 = df1.query(filtro)
	cols[3].dataframe(df2['nome_dia'].value_counts())	

	filtro = 'raio_m>0'
	cols[4].write(filtro)
	df2 = df1.query(filtro)
	cols[4].dataframe(df2['nome_dia'].value_counts())

	filtro = 'raio_m==0'
	cols[5].write(filtro)
	df2 = df1.query(filtro)
	cols[5].dataframe(df2['nome_dia'].value_counts())


with tab2:
	cols = st.columns([1,1,1,1])	
	filtro = 'raio_m>0'
	cols[2].write(filtro)
	df2 = df1.query(filtro)
	cols[2].dataframe(df2['nome_dia'].value_counts())

	filtro = 'raio_m==0'
	cols[3].write(filtro)
	df2 = df1.query(filtro)
	cols[3].dataframe(df2['nome_dia'].value_counts())

	st.write('dia')
	st.write('noite')
	st.write('madrugada')

	#st.dataframe(df2['hora'].value_counts().sort_index())
with tab3:
	st.write('primeira hora do dia que a chave ligou')
	#inicio = df1[df1['atividade'] == 'chave_ligada']['hora'].iloc[0]
	#st.dataframe(inicio)

with tab4:
	st.write('ultima hora hora do dia que a chave desligou')

with tab5:
	st.write('tab5')


#filtro = 'motor_ligado==False'
#st.write('Improdutiva: '+filtro)
#df2 = df1.query(filtro)
