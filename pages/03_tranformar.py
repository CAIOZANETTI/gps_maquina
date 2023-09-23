import streamlit as st
import pandas as pd
import math

import fx_streamlit as fx_streamlit

#todo
def check_motor_ligado(atividades:list)->list:
	status =[]
	ligado=0
	for atividade in atividades:
		if atividade=='chave_ligada':
			ligado = 1
		elif atividade=='chave_desligada':
			ligado =0
		status.append(ligado)
	return status

def haversine_distance(lat1:float, lon1:float, lat2:float, lon2:float)->float:
	lat1 = math.radians(lat1)
	lon1 = math.radians(lon1)
	lat2 = math.radians(lat2)
	lon2 = math.radians(lon2)
	    
	# Radius of the Earth in meters
	earth_radius = 6371000  # Approximate value
	    
	# Haversine formula
	dlat = lat2 - lat1
	dlon = lon2 - lon1
	a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
	distance = round(earth_radius * c,0)
	
	return distance

def url_to_coordenadas(url:str)->list:
	""" 
	url_to_coordenadas: 
	input:'("http://maps.google.com/?q=-26,6069566,-51,0962178","-26,6069566,-51,0962178")'
	output:[-26.6069566,-51.0962178]
	"""
	start_index = url.find("q=") + 2
	end_index = url.find('","')

	substring = url[start_index:end_index] 
	parts = substring.split(',') #['-26', '6066705', '-51', '0989749']

	lst_out = [0,0]
	if len(parts)==4:
		lst_out[0] = parts[0]+'.'+parts[1]
		lst_out[1] = parts[2]+'.'+parts[3]
		lst_out = [float(num) for num in lst_out]

	return lst_out

def df_bronze_to_silver_gps(remover_colunas:list,df)->pd.DataFrame:
	"""
	converter: data, hora e latitude e longitude
	obter colual: hora, nome_dia,lat_lon
	"""
	df['data_hora'] = pd.to_datetime(df['data_hora'], format='%m/%d/%Y %H:%M:%S')
	df['data'] = df['data_hora'].dt.date
	df['hora'] = df['data_hora'].dt.hour
	df['nome_dia'] = df['data_hora'].dt.day_name().str.lower()
	df['atividade'] = df['atividade'].str.lower().str.replace(' ', '_')

	#normalizar gps
	df['lat'], df['lon'] = zip(*df['maps_google_url'].apply(url_to_coordenadas))
	df['lat_lon'] = df['lat'].astype(str) + '|' + df['lon'].astype(str)

	#calcular distancia
	df['lat_ant'] = df['lat'].shift(1)
	df['lon_ant'] = df['lon'].shift(1)
	df['raio_m'] = df.apply(lambda row: haversine_distance(row['lat_ant'], row['lon_ant'], row['lat'], row['lon']), axis=1)

	#motor ligado
	atividades = df['atividade'].tolist()
	df['motor_ligado'] = check_motor_ligado(atividades)

	#converter colunas object to string
	df = df.astype({'nome_dia': 'string','lat_lon':'string','atividade':'string'})


	#remover colunas
	for coluna in remover_colunas:
		if coluna in df.columns:
			df = df.drop(coluna,axis=1)
	return df

def df_silver_to_gold_motor_ligado(df:pd.DataFrame)->pd.DataFrame:
	#todo fazer ...

	df1 = df
	return df1

# carregar ou ler silver
if 'df1' not in st.session_state:
	df1 = pd.read_parquet('data/silver_jcb_relatorio_2022.parquet',engine='pyarrow')
else:
	df = st.session_state['df']
	remover_colunas = ['id','hyperlink','maps_google_url']
	df1 = df_bronze_to_silver_gps(df=df,remover_colunas=remover_colunas)
st.session_state['df1'] = df1

# carregar ou download silver
btn_reload = st.button('recarregar')
if btn_reload == True:
	df = pd.read_parquet('data/bronze_jcb_relatorio_2022.parquet',engine='pyarrow')
	remover_colunas = ['id','hyperlink','maps_google_url']
	df1 = df_bronze_to_silver_gps(df=df,remover_colunas=remover_colunas)
	st.session_state['df1'] = df1

#download
parquet = df1.to_parquet('silver_jcb_relatorio_2022.parquet', index=False)
btn_download = st.download_button('download',parquet,'silver_jcb_relatorio_2022.parquet')

#mostrar analise
fx_streamlit.analise_df(df1,'silver....')

#teste
st.write('some info')