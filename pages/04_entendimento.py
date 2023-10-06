import datetime
import streamlit as st
import pandas as pd
#from datetime import datetime

import fx_streamlit as fx_streamlit


#carregar df1
if 'df1' not in st.session_state:
	df1 = pd.read_parquet('data/silver_jcb_relatorio_2022.parquet',engine='pyarrow')
	st.session_state['df1'] = df1
df1 = st.session_state['df1']


with st.expander('periodo disponivel no dataframe',expanded=True):
	st.dataframe(df1)
	#cols = st.columns([1,1])
	#cols[0].write('inicio: ' +str(df1['data'].min()))
	#cols[1].write('fim: ' +str(df1['data'].min()))

