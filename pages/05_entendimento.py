import streamlit as st
import pandas as pd

st.subheader("Entendimento")

st.write(
'A compreender as informações dos dados\
identificar quais informações são relevantes,\
como elas estão distribuídas, qual a relação\
entre demais variáveis como o tempo (hora, dia, mês)\
ou coordenadas lat+lon.')

# atividades....
#tab1,tab2,tab3,tab4 = st.tabs(['atividade_unicas','dias'])

if 'df1' not in st.session_state:
	df1 = pd.DataFrame()
	st.write('df1 esta vazio!!! voltar e transformar')

df1 = st.session_state['df1']


st.dataframe(df1.head(2))

df2 = df1['atividade'].value_counts().reset_index()
df2.columns = ['atividade','qtd']
qtd_min = int(round(df2['qtd'].min(),0))
qtd_max = int(round(df2['qtd'].max(),0))


#st.write(qtd_min,type(qtd_min))


st.dataframe(df2.head(2))

#st.write(df2.describe())


st.data_editor(
    df2,
    column_config={
        "qtd": st.column_config.ProgressColumn(
            "quantity",
            width='large',
            format='%f',
            min_value=qtd_min,
            max_value=qtd_max,
        ),
    },
    hide_index=True,
)



