import streamlit as st
import pandas as pd


if 'df1' not in st.session_state:
	df1 = pd.read_parquet('data/silver_jcb_relatorio_2022.parquet',engine='pyarrow')
	st.session_state['df1'] = df1

df1 = st.session_state['df1']


with st.expander('info',expanded=False):
	st.markdown('comportamento produtivo, inprodutivo, previsto, adequado, improvavel')

tab1,tab2,tab3,tab4,tab5 = st.tabs(['produtivo','tab2','tab3','tab4','tab5'])

filtro = 'motor_ligado==True'
st.write('Produtiva: '+filtro)
df2 = df1.query(filtro)

with tab1:
	st.write('vazio')
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
