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
	cols[2].metric(label="Media **dias**", value=media, delta=desvio)

with st.expander('**Horas** disponiveis no periodo', expanded=False):
	st.write('divisão do dia em 4 periodos (quartil) de 6 horas')
	cols = st.columns([1,1])
	#df
	df_hours = analise.count_hours()
	cols[0].dataframe(df_hours)

	#total
	total_quartil = fx_data.str_milhar(analise.horas_uteis_quartil)
	total = fx_data.str_milhar(analise.horas_uteis_quartil*2)
	
	cols[1].metric(label='Total **hora produtiva**',value=total+'h', delta=total_quartil+'h quartil')

with st.expander('**Anos** e **Meses** disponiveis no periodo', expanded=False):
	
	analise.count_year_months()
	cols = st.columns([1,1,1,1])

	cols[0].write(analise.df_anos)
	cols[1].dataframe(analise.df_mes)
	cols[2].dataframe(analise.df_ano_mes)
	#resultado
	cols[3].metric('Total ano_mes',analise.qtd_ano_mes,str(analise.qtd_ano)+' anos')
	

with st.expander('Resultado **dias, horas, meses e anos**', expanded=True):
	
	cols = st.columns([1,1,1])
	cols[0].metric(label="Media **dias**", value=media, delta=desvio)
	cols[1].metric(label='Total **hora produtiva**',value=total+'h', delta=total_quartil+'h quartil')
	cols[2].metric('Total **ano_mes**',analise.qtd_ano_mes,str(analise.qtd_ano)+' anos')
