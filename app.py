import streamlit as st

with st.sidebar:
	st.radio('idioma dos comentarios', ['portugues','ingles'],key='idioma')
	st.text(st.session_state['idioma'])


