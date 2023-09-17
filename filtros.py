import pandas as pd
from datetime import datetime


def df_periodo(df:pd.DataFrame,inicio,fim)->pd.DataFrame:
	df['data'] = df['data_hora'].dt.date

	df1 = df[(df['data']>= inicio) & (df['data']<= fim)]

	return df1
