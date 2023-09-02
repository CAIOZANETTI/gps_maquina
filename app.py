import datetime
import streamlit as st

#modulos
import listas as lst
import extrair
import caminhos

hoje={}
hoje['datetime'] = datetime.datetime.now()
hoje['data'] = hoje['datetime'].date()
hoje['hora'] = hoje['datetime'].time()

with st.sidebar:
	cols = st.columns([1,1])
	cols[0].text(hoje['data'])
	cols[1].text(hoje['hora'])
	
	with st.expander('usuario',expanded=True):
		st.selectbox("usuarios",lst.usuarios,key='usuario')
		st.write(st.session_state['usuario'])

caminho =caminhos.tabelas['jcb_relatorio'] 
st.write(caminho)

df = extrair.gsheet_to_df(
	id = caminho['id'],
	tabela=caminhó['tabela'],
	testar=False)

st.dataframe(df)




