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

tab1,tab2,tab3,tab4,tab5 = st.tabs(['dias','dias','horas prod','inicio','termino'])


with tab1:

	with st.expander('querys', expanded=False):
		querys = {
		'motor_on':'motor_ligado==True',
		'motor_off':'motor_ligado==False',
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
		st.dataframe(df_med)

with tab2:

	st.write('querys')
	
with tab3:
	st.write('primeira hora do dia que a chave ligou')
	#inicio = df1[df1['atividade'] == 'chave_ligada']['hora'].iloc[0]
	#st.dataframe(inicio)

with tab4:
	st.write('ultima hora hora do dia que a chave desligou')

with tab5:
	st.write('tab5')


#filtro = 'motor_ligado==False'
#st.write('Improdutiva: '+filtro)
#df2 = df1.query(filtro)
