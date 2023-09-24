import streamlit as st
import pandas as pd
import fx_streamlit as fx_streamlit


if 'df1' not in st.session_state:
	df1 = pd.read_parquet('data/silver_jcb_relatorio_2022.parquet',engine='pyarrow')
	st.session_state['df1'] = df1

df1 = st.session_state['df1']

#idioma
cols = st.columns([1,1])
idioma = cols[0].radio('idioma dos comentarios', ['portugues','ingles'])
textos = fx_streamlit.textos('05_entendimento',idioma)

#introdução
cols[1].subheader(textos['atividade'] )
st.markdown(textos['introducao'])

# atividades....
st.subheader(textos['atividade'])
st.markdown(textos['contagem'])

tab1,tab2,tab3,tab4 = st.tabs(['contagem','principal','amostra','conclusao'])

with tab1: #contagem
	df2 = df1['atividade'].value_counts().reset_index()
	df2.columns = ['atividade','qtd']
	df2['perc'] = round(100*(df2['qtd']/df2['qtd'].sum()),0)
	df2['perc'] = df2['perc'].astype(int)
	df2['util'] = df2['perc']>5	
	st.dataframe(df2)

with tab2: #principal
	st.dataframe(df2[df2['util']==True])

with tab3: #amostra
	st.dataframe(df2.iloc[2:100])	


with tab4: #conclusao
	st.markdown(textos['conclusao'])


#st.write('interpretação')
#st.write('para determinar a ')