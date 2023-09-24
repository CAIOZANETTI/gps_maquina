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


def textos(pagina:str,idioma:str)->dict:
	#todo: para melhorar e dividir o serviço podemos incluir em formato json

	if pagina =='05_entendimento':
		dic = {}
		if idioma =='portugues':
			dic['titulo'] = "Entendimento"
			dic['atividade'] = "atividades"
			dic['introducao']="""
				Para aprimorar a compreensão dos dados,
			 	é essencial **identificar quais informações são pertinentes**,
			  	analisar sua distribuição e explorar as relações existentes com
			   outras variáveis, como o **tempo (hora, dia, mês)** e coordenadas
			   geográficas (latitude e longitude).
			   """

			dic['contagem'] = """
				Para aprimorar a compreensão dos dados, 
				é crucial **realizar uma análise da coluna de atividades**, 
				utilizando um filtro para identificar aquelas que são 
				**mais frequentes e relevantes**.
				"""
			dic['conclusao'] ="""A atividade **'chave_ligada'** e **'chave_desligada'** determina o range de funcionamento do equipamento. A partir disso, foi incluída a coluna de **'motor_ligado'** para determinar o período em que a máquina esteve em funcionamento (valor 1) e desligada (valor 0)."""

		elif idioma=='ingles':
			dic['titulo'] = "understanding"
			dic['atividade'] = "activities"
			dic['introducao']="""To enhance data understanding,
				 it is essential to **identify which information is relevant**,
				 analyze its distribution, and explore the relationships with other variables,
				  such as **time (hour, day, month)** and geographical coordinates (latitude and longitude)."""

			dic['contagem'] = 'To enhance data understanding, it is crucial to **perform an analysis of the activities column**, using a filter to identify those that are **more frequent and relevant**.'

			dic['conclusao'] = """ The **'chave_ligada'** and **'chave_desligada'** activities determine the operating range of the equipment. Subsequently, the **'motor_ligado'** column was included to determine the period during which the machine was in operation (value 1) and turned off (value 0)."""

		return dic

	else:
		dic = {}
		return dic