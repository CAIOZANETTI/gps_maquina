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
	summary.drop(['25%', '50%', '75%'], inplace=False)
	cols[1].dataframe(summary)
	#resultado
	media = analise.qtd_med_weekdays
	desvio =analise.std_med_weekdays
	cols[2].metric(label="Media **adotada**", value=media, delta=desvio)

with st.expander('**Horas** disponiveis no periodo', expanded=False):
	st.write('divisão do dia em 4 periodos (quartil) de 6 horas')
	cols = st.columns([1,1])
	#df
	df_hours = analise.count_hours()
	cols[0].dataframe(df_hours)

	#total
	total_quartil = fx_data.str_milhar(analise.horas_uteis_quartil)
	total = fx_data.str_milhar(analise.horas_uteis_quartil*2)
	
	cols[1].metric(label='Total horas util',value=total+'h', delta=total_quartil+'h quartil')

with st.expander('periodo em **meses**', expanded=True):
	st.write('meses')

	cols = st.columns([1,1])

	df_mes = analise.count_months()
	cols[0].dataframe(df_mes)
	cols[1].write(analise.qtd_meses)
	cols[1].write(analise.qtd_anos)

with st.expander('periodo em **anos**', expanded=False):
	st.write('anos')

