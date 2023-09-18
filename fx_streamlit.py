
import streamlit as st

def analise_df(df):

	tab1,tab2,tab3,tab4,tab5 = st.tabs(['dataframe','describe','shape','columns','bytes'])

	with tab1:
		st.dataframe(df)

	with tab2:
		st.write(df.describe())

	with tab3:
		shape = {}
		shape['rows'] = df.shape[0]
		shape['columns'] = df.shape[1]
		st.write(shape)

	with tab4:
		st.write(df.dtypes)

	with tab5:
		memory = {}
		memory['bytes'] = int(df.memory_usage(deep=True).sum())
		memory['Kb'] = round(memory['bytes'] / 1024,2)
		memory['Mb'] = round(memory['bytes'] / 1048576,2)
		
		st.write(memory)

	st.session_state['df'] = df