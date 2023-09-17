import datetime
import pytz

import streamlit as st
import pandas as pd

#modulos
import listas as lst
import extrair
import caminhos
import funcoes_gps


brazil_tz = pytz.timezone('America/Sao_Paulo')
hoje={}
hoje['datetime'] = datetime.datetime.now(brazil_tz)
hoje['data'] = hoje['datetime'].date()
hoje['hora'] = hoje['datetime'].time()

with st.sidebar:
	cols = st.columns([1,1])
	cols[0].text(hoje['data'])
	cols[1].text(hoje['hora'])
	
	st.selectbox("usuarios",lst.usuarios,key='usuario')
	st.write(st.session_state['usuario'])

	st.radio("relatorios",['mapas','tabelas','graficos'],key='relatorios')

  
    

if st.session_state['relatorios']== 'mapas':
	st.write('mapas')

if st.session_state['relatorios']== 'tabelas':
	st.write('tabelas')

if st.session_state['relatorios']== 'graficos':
	st.write('graficos')