import pandas as pd
from datetime import datetime


def df_periodo(df:pd.DataFrame,inicio,fim)->pd.DataFrame:
	
	if not isinstance(inicio, datetime):
		inicio = datetime.strptime(inicio, "%Y-%m-%d")
	if not isinstance(fim, datetime):
		fim = datetime.strptime(fim, "%Y-%m-%d")
	df1 = df[(df['data_hora']>= inicio) & (df['data_hora']<= fim)]

	return df1
