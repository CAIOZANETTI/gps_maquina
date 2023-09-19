import streamlit as st

st.header("Filtrar")


tab1,tab2,tab3 = st.tabs(['1-periodo','2-atividades','3-dia-semana'])

with tab1:
	st.text('disponivel: jan/2022 -> ago/2022')
	st.date_input('inicio',datetime.datetime(2022,1,1),key='inicio')
	st.date_input('fim',datetime.datetime(2022,1,8),key='fim')

with tab2:
	st.write('atividades')

with tab3:
	st.write('dia da semana')
