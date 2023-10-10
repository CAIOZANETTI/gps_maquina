import datetime
import streamlit as st
import pandas as pd

import fx_data as fx_data
import fx_streamlit as fx_streamlit


#carregar df1
if 'df1' not in st.session_state:
	df1 = pd.read_parquet('data/silver_jcb_relatorio_2022.parquet',engine='pyarrow')
	st.session_state['df1'] = df1
df1 = st.session_state['df1']

#inicar classe de Analise
analise = fx_data.PeriodoDataFrame(df1)

with st.expander('**Dias da semana** disponiveis no dataframe', expanded=False):
	cols = st.columns([2,1,1])
	
	#df
	df_weekdays = analise.count_weekdays()
	cols[0].dataframe(df_weekdays)
	#sumario
	summary = df_weekdays.describe()
	summary.drop(['25%', '50%', '75%'], inplace=True)
	cols[1].dataframe(summary)
	#resultado
	media = analise.qtd_med_weekdays
	desvio =analise.std_med_weekdays
	cols[2].metric(label="Media **adotada**", value=media, delta=desvio)

with st.expander('**Horas** disponiveis no periodo', expanded=True):
	st.write('divisão do dia em 4 periodos iguais de 6 horas')
	cols = st.columns([2,1,1])
	#df
	df_hours = analise.count_hours()
	cols[0].dataframe(df_hours)

	#total
	total = analise.horas_uteis_quartil
	cols[2].metric(
		label="**Total horas **",
		value=str(total*2)+' util', 
		delta=str(total*2)+' periodo')

with st.expander('periodo em **meses**', expanded=False):
	st.write('meses')

with st.expander('periodo em **anos**', expanded=False):
	st.write('anos')

