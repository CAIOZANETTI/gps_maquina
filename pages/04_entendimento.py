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




with st.expander('periodo em **horas**', expanded=False):
	st.write('horas')

with st.expander('periodo em **dias**', expanded=True):
	analise = fx_data.PeriodoDataFrame(df1)
	df_weekdays = analise.count_weekdays()
	cols = st.columns([1,1])
	cols[0].dataframe(df_weekdays)
	cols[1].write(df_weekdays.describe())


with st.expander('periodo em **meses**', expanded=False):
	st.write('meses')

with st.expander('periodo em **anos**', expanded=False):
	st.write('anos')

