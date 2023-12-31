
import streamlit as st
import pandas as pd

import fx_data as fx_data


if 'df1' not in st.session_state:
	df1 = pd.read_parquet('data/silver_jcb_relatorio_2022.parquet',engine='pyarrow')
	st.session_state['df1'] = df1

df1 = st.session_state['df1']
periodo = fx_data.PeriodoDataFrame(df1)

st.subheader('Analise a rotina da retroescavadeira em que foi **ligada**')
filtro = 'atividade == "chave_ligada"'
#st.write(filtro)

tab1,tab2 = st.tabs(['dia','hora'])

with tab1: #dias chave_on
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

with tab2:
	with st.expander('Quantidade **Total** chave_on por **hora**', expanded=False):
		filtro = 'atividade == "chave_ligada" and nome_dia != "saturday" and nome_dia!="sunday"' 
		st.write(filtro)
		df2= df1.query(filtro)
		
		df2 = df2['hora'].value_counts().reset_index()
		df2 = df2.fillna(0)
		df2 = df2.replace('None',0)
		df2['count'] = df2['count'].astype(int)


		#ordenar index
		ordem_index =  list(range(0, 23))
		df2.set_index('hora',inplace=True)

		df2 = df2.reindex(ordem_index)
		st.dataframe(df2.T)
	
	with st.expander('Grafico **barras** qtd **Total**', expanded=False):
		st.bar_chart(df2)
	with st.expander('grafico **linhas** qtd **Total**', expanded=False):
		st.line_chart(df2)

	with st.expander('qtd **Média** chave_on por **hora/dia**', expanded=False):	
		st.markdown('qtd **dias uteis** : '+str(periodo.qtd_total_weekdays))
		df2 = df2.query('count>0')
		total_horas = df2['count'].sum()	
		df2['qtd_dia'] = round(df2['count']/periodo.qtd_total_weekdays,1)
		df3 = df2
		df3 = df3.query('qtd_dia>0')
		df3 = df3.drop('count', axis=1)
		st.bar_chart(df3)
		st.dataframe(df3.T)

	with st.expander('qtd **Média** chave_on por **hora/dia**', expanded=False):
		df4 = df3.query('qtd_dia>1')
		st.dataframe(df4.T)
		df_sumary =df4.describe() 
		st.dataframe(df_sumary.T)

	with st.expander('Resultado Quantidade **Chave Ligada**', expanded=True):
		qtd_med_chave_on_hora =df_sumary['qtd_dia'].loc['75%']
		qtd_hora_dias =df_sumary['qtd_dia'].loc['count'] 
		
		cols = st.columns([1,1,1])

		cols[0].metric(
			'Média **hora/dia**',
			str(qtd_med_chave_on_hora)+' x',
			str(qtd_hora_dias)+' h')

		lst_hora = df4.index.values.tolist()
		lst_qtd = df4['qtd_dia'].values.tolist()
		#st.write(lst[0],lst[-1])

		cols[1].metric('Média hora **Inicio**',
			str(lst_hora[0])+' h',
			str(lst_qtd[0])+' x')

		cols[2].metric('Média hora **Fim**',
			str(lst_hora[-1])+' h',
			str(lst_qtd[-1])+' x')
