
import streamlit as st
import pandas as pd

import fx_data as fx_data


if 'df1' not in st.session_state:
	df1 = pd.read_parquet('data/silver_jcb_relatorio_2022.parquet',engine='pyarrow')
	st.session_state['df1'] = df1

df1 = st.session_state['df1']

with st.expander('info',expanded=False):
	st.markdown('analisar a rotina da retro escavadeira nos momentos em que foi **ligada**')
	filtro = 'atividade == "chave_ligada"'
	st.write(filtro)

tab1,tab2,tab3,tab4,tab5 = st.tabs(['periodo','dias chave_on','horas chave_on','inicio','termino'])

with tab1:
	st.write('vazio')
	

with tab2: #dias chave_on
	
	with st.expander('analise de atividades vs qtd dias **Total**', expanded=True):
		ordem_index = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

		df2 = df1.query(filtro)
		df2 = df2['nome_dia'].value_counts().reset_index()
		#df2.set_index()


		#df2 = fx_data.df_count_query_merge(df=df1,coluna='nome_dia',ordem_index=ordem_index,querys=filtro)
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
		cols[1].metric('Qtd Média Dia **Util**',media_dia_util,desvio)


with tab3:
	with st.expander('qtd **Total** chave_on por **hora**', expanded=True):
		filtro = 'atividade == "chave_ligada" and nome_dia != "saturday" and nome_dia!="sunday"' 
		st.write(filtro)
		df2= df1.query(filtro)
		
		df2 = df2['hora'].value_counts().reset_index()
		df2 = df2.fillna(0)
		df2 = df2.replace('Nome',0)
		
		#ordenar index
		ordem_index =  list(range(0, 23))
		df2.set_index('hora',inplace=True)
		df2 = df2.reindex(ordem_index)

		st.dataframe(df2.T)

	with st.expander('qtd **dias uteis**', expanded=True):
		df2 = df1.query(filtro)
		df_data = df2['data'].unique()
		st.write(df_data.shape)
		st.write(df_data)

		st.write('qtd **dias uteis** no periodo = '+str(160))

	with st.expander('qtd **Média** chave_on por **hora**', expanded=True):	
		
		df3 = pd.DataFrame()
		df3 = round(df2/media_dia_util,0)
		st.dataframe(df3.T)
	
with tab4:
	st.write('primeira hora do dia que a chave ligou')
	#inicio = df1[df1['atividade'] == 'chave_ligada']['hora'].iloc[0]
	#st.dataframe(inicio)

with tab5:
	st.write('ultima hora hora do dia que a chave desligou')


#filtro = 'motor_ligado==False'
#st.write('Improdutiva: '+filtro)
#df2 = df1.query(filtro)
