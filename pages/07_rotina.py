import streamlit as st
import pandas as pd

import fx_data as fx_data


if 'df1' not in st.session_state:
	df1 = pd.read_parquet('data/silver_jcb_relatorio_2022.parquet',engine='pyarrow')
	st.session_state['df1'] = df1

df1 = st.session_state['df1']

with st.expander('info',expanded=False):
	st.markdown('analisar a rotina da maqiona no periodo disponivel no dataframe,\
	 afim de identificar algum padrão que possa ser caracterizado como um comportamento')

tab1,tab2,tab3,tab4,tab5 = st.tabs(['chave_on vs dias','horas','horas prod','inicio','termino'])

with tab1:

	with st.expander('querys', expanded=False):
		querys = {
		'motor_on':'atividade == "arranque_do_motor"',
		'motor_off':'atividade == "paragem_do_motor"',
		'chave_on':'atividade == "chave_ligada"',
		'chave_off':'atividade == "chave_desligada"',
		}
		st.write(querys)
	
	with st.expander('analise de atividades vs qtd dias **Total**', expanded=False):
		df2 = fx_data.df_count_query_merge(df1,'nome_dia',querys)
		st.dataframe(df2)
	
	with st.expander('analise de atividades vs qtd dias **Média**', expanded=False):
		df_dia = fx_data.count_weed_by_name('2022-01-01','2022-08-01')
		st.dataframe(df_dia.T)

		df3 = df2.div(df_dia['qtd'],axis=0).astype(int)
		st.dataframe(df3)
	
	with st.expander('Quantidade **Média** acionamento da Maquina por **dia**', expanded=False):
		df_med = df3.median(axis=1).astype(int)
		cols = st.columns([1,4])
		cols[0].dataframe(df_med)
		cols[1].bar_chart(df_med)

	with st.expander('Quantidade **Média dia util**', expanded=True):
		df_med= df_med.reset_index()
		df_med.columns=['nome_dia','count']
		df_med['dia_util']=True
		df_med.loc[df_med['nome_dia'].isin(['saturday', 'sunday']), 'dia_util'] = False
		cols = st.columns([1,1])
		cols[0].write('Todos os dias')
		cols[0].dataframe(df_med)
		
		cols[1].write('Dias Uteis')
		df_med_util = df_med.query('dia_util==True')
		cols[1].dataframe(df_med_util)
	
		media_dia_util = df_med_util['count'].median()
		desvio = round(df_med_util['count'].std(),0)
		st.metric('Qtd Média Dia **Util**',media_dia_util,desvio)


with tab2:
	st.write('querys')
	
with tab3:
	st.write('primeira hora do dia que a chave ligou')
	#inicio = df1[df1['atividade'] == 'chave_ligada']['hora'].iloc[0]
	#st.dataframe(inicio)

with tab4:
	st.write('ultima hora hora do dia que a chave desligou')

with tab5:
	st.write('tab5 R$257,25')


#filtro = 'motor_ligado==False'
#st.write('Improdutiva: '+filtro)
#df2 = df1.query(filtro)
