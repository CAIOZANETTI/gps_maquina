import streamlit as st
import listas as lst

st.write("teste")
st.write(nomes.variavel)

with st.sidebar:
	with st.expander('usuario',expanded=True)
		st.selectbox("usuarios",lst.usuarios,key='usuario')
		st.write(st.session_state['usuario'])



