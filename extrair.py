import json
import pandas as pd

def json_to_dic(json_file_path:str,nome:str)->dict:

	with open(json_file_path, 'r') as json_file:
		dic = json.load(json_file)
	return dic


def gsheet_to_df(id:str,tabela:str,testar:bool)->pd.DataFrame:
	if testar==True:
		id = '1QRZMLdzTA07yajuaYN936NrSMx8WonPi8iE4P73WBVM'
		tabela = "cotacao"
	
	try: #formato excel
		gsheet_url = f"https://docs.google.com/spreadsheets/d/{id}/export?format=xlsx"
		xlsx= pd.ExcelFile(gsheet_url)
		df=pd.read_excel(xlsx,tabela,header=1)
		return df
	
	except: #formato csv
		gsheet_url = f"https://docs.google.com/spreadsheets/d/{id}/gviz/tq?tqx=out:csv&sheet={tabela}"
		df = pd.read_csv(gsheet_url)
		print(tabela+'.csv cuidado com virgula(,) e ponto(.)')
		return df

def excel_to_df():
	return df

def csv_to_df():
	return df	

def mongodb_to_df():
	return df

def mysql_to_df():
	return df