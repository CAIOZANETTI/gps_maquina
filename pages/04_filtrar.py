import datetime
import streamlit as st

st.header("Filtrar")


tab1,tab2,tab3 = st.tabs(['1-periodo','2-atividades','3-dia da semana'])

with tab1:
	st.text('disponivel: jan/2022 -> ago/2022')
	st.date_input('inicio',datetime.datetime(2022,1,1),key='inicio')
	st.date_input('fim',datetime.datetime(2022,1,8),key='fim')

	dias = st.session_state['fim'] - st.session_state['inicio']
	dias = dias.days
	if dias>0:
		st.write('Periodo: '+str(dias)+' dias')
	elif dias<0:
		st.write('NEGATIVO REVISAR '+str(dias)+' dias')

with tab2:
	st.write('atividades')

with tab3:
	st.write('dia da semana')
