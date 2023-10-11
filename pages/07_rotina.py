
import streamlit as st
import pandas as pd

import fx_data as fx_data


if 'df1' not in st.session_state:
	df1 = pd.read_parquet('data/silver_jcb_relatorio_2022.parquet',engine='pyarrow')
	st.session_state['df1'] = df1

df1 = st.session_state['df1']
periodo = fx_data.PeriodoDataFrame(df1)


with st.expander('Chave **Ligada**',expanded=False):
	st.markdown('analisar a rotina da retroescavadeira nos momentos em que foi **ligada**')
	filtro = 'atividade == "chave_ligada"'
	st.write(filtro)

tab1,tab2,tab3,tab4,tab5 = st.tabs(['vazio','dia','hora','inicio','termino'])

with tab1:
	st.write('vazio')
	

with tab2: #dias chave_on
	with st.expander('analise Periodo disponivel em dias vs **chave on**', expanded=False):
		
		cols = st.columns([1,1])
		#periodo
		df_weekdays = periodo.count_weekdays()
		cols[0].dataframe(df_weekdays)
		#filtro
		#st.dataframe(df1)
		df2 = df1.query(filtro)
		df2 = df2['nome_dia'].value_counts().reset_index()
		df2.columns = ['nome_dia','chave_on_total']
		#index
		df2.set_index('nome_dia',inplace=True)
		ordem_index = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
		df2 = df2.reindex(index=ordem_index)
		#df2 = df2.fillna(0)
		cols[1].dataframe(df2)
	
	with st.expander('analise de atividades vs qtd dias **Média**', expanded=False):
		df3 = pd.merge(df2,df_weekdays,on='nome_dia',how='outer')
		df3['chave_on_dia'] = round(df3['chave_on_total']/df3['qtd'],2)
		st.dataframe(df3)
	
	with st.expander('Grafico e tabela de **Média**', expanded=False):
		cols = st.columns([1,2])
		cols[0].dataframe(df3['chave_on_dia'])
		cols[1].bar_chart(df3['chave_on_dia'])

	with st.expander('Quantidade **Média dia util ou Produtivo**', expanded=False):
		df4 = df3.query('dia_util==True')
		st.dataframe(df4)		

	with st.expander('Resultado Quantidade **Média dia util ou Produtivo**', expanded=True):
		med_chave_on_dia = int(df4['chave_on_dia'].median())
		variacao = round(df4['chave_on_dia'].median()-med_chave_on_dia,2)
		st.metric('Chave_on **(Ligado)**',str(med_chave_on_dia)+'x  /dia',variacao)

with tab3:
	with st.expander('qtd **Total** chave_on por **hora**', expanded=True):
		filtro = 'atividade == "chave_ligada" and nome_dia != "saturday" and nome_dia!="sunday"' 
		st.write(filtro)
		df2= df1.query(filtro)
		
		df2 = df2['hora'].value_counts().reset_index()
		df2 = df2.fillna(0)
		df2 = df2.replace('None',0)
		
		#ordenar index
		ordem_index =  list(range(0, 23))
		df2.set_index('hora',inplace=True)

		df2 = df2.reindex(ordem_index)
		st.dataframe(df2.T)

	with st.expander('qtd **Média** chave_on por **hora**', expanded=True):	
		st.markdown('qtd **dias uteis**')
		st.write(periodo.qtd_total_weekdays)
		
		df3 = df2/periodo.qtd_total_weekdays
		df3['valido'] = (df3['count']>0).astype(bool)

		st.dataframe(df3.T)
	
with tab4:
	st.write('primeira hora do dia que a chave ligou')
	

with tab5:
	st.write('ultima hora hora do dia que a chave desligou')

