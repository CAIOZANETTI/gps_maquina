import streamlit as st
import pandas as pd

import fx_streamlit as fx_streamlit



if 'df1' not in st.session_state:
	df1 = pd.read_parquet('data/silver_jcb_relatorio_2022.parquet',engine='pyarrow')
	st.session_state['df1'] = df1

df1 = st.session_state['df1']

st.subheader('Analise **Comportamentos**: produtivo, improdutivo, previsto, adequado, improvavel')

tab1,tab2,tab3,tab4,tab5 = st.tabs(['improvalvel','tab2','tab3','tab4','tab5'])


with tab1:
	st.markdown('motor foi ligado em dia de **folga**')
	filtro = [
	'(motor_ligado==True) and (nome_dia=="sunday")',
	'(motor_ligado==True) and (nome_dia=="saturday")and (hora>13)',
	'(motor_ligado==True) and (hora>18)',
	'(motor_ligado==True) and (hora>0) and (hora<6)'
	]
	st.selectbox('comportamento',filtro, key='filtro')
	df2 = df1.query(st.session_state['filtro'])
	
	fx_streamlit.analise_df(df2,st.session_state['filtro'])
	st.dataframe(df2)

with tab2:
	st.write('vazio')

with tab3:
	st.write('vazio')

with tab4:
	st.write('vazio')

with tab5:
	st.write('vazio')


filtro = 'motor_ligado==False'
st.write('Improdutiva: '+filtro)
df2 = df1.query(filtro)
