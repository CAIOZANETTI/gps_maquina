import streamlit as st
import fx_data as fx_data

def analise_df(df,nome):

	st.write('**info** dataframe : '+nome)

	tab1,tab2,tab3,tab4,tab5,tab6,tab7 = st.tabs(['dtypes','dataframe','table','shape','describe','bytes','analise'])

	with tab1:
		st.write(df.dtypes)

	with tab2:
		st.dataframe(df)

	with tab3:
		#st.write('st.table esta ficando lento')
		st.table(df.head(5))

	with tab4:
		shape = {}
		shape['rows'] = df.shape[0]
		shape['columns'] = df.shape[1]
		st.write(shape)

	with tab5:
		st.write(df.describe())

	with tab6:
		memory = {}
		memory['bytes'] = int(df.memory_usage(deep=True).sum())
		memory['Kb'] = round(memory['bytes'] / 1024,2)
		memory['Mb'] = round(memory['bytes'] / 1048576,2)
		
		st.write(memory)

	with tab7:
		dic = fx_data.analise_dataframe(df)

		for k,v in dic.items():
			st.markdown("""---""")
			st.write(k,v)
