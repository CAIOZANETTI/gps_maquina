import streamlit as st
import listas as lst
import datetime

hoje['datetime'] = datetime.datetime.now()
hoje['data'] = hoje['datetime'].date()
hoje['hora'] = hoje['datetime'].time()

with st.sidebar:
	with st.expander('usuario',expanded=True):
		cols = st.columns([1,1])
		cols[0].text(hoje['data'])
		cols[1].text(hoje['hora'])

		st.selectbox("usuarios",lst.usuarios,key='usuario')
		st.write(st.session_state['usuario'])



