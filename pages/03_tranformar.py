import streamlit as st
import pandas as pd
import math

def haversine_distance(lat1:float, lon1:float, lat2:float, lon2:float)->float:
    # Example usage
	"""
    chat gpt 3.5
    Calculate the distance between two points on the Earth's surface
    using the Haversine formula.
    
    :param lat1: Latitude of the first point (in degrees)
    :param lon1: Longitude of the first point (in degrees)
    :param lat2: Latitude of the second point (in degrees)
    :param lon2: Longitude of the second point (in degrees)
    :return: Distance between the two points in meters
   """
	
	# Convert latitude and longitude from degrees to radians
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

	df['lat'], df['lon'] = zip(*df['maps_google_url'].apply(url_to_coordenadas))
	df['lat_lon'] = df['lat'].astype(str) + '|' + df['lon'].astype(str)

	#converter colunas em string
	colunas_str ={'nome_dia': 'string','lat_lon':'string','atividade':'string'}
	df.astype(colunas_str).dtypes

	#remover colunas
	for coluna in remover_colunas:
		if coluna in df.columns:
			df = df.drop(coluna,axis=1)
	return df

df = st.session_state['df']
remover_colunas = ['id','hyperlink','maps_google_url']
df = df_bronze_to_silver_gps(df=df,remover_colunas=remover_colunas)

st.header("Tranformar - Silver")
fx_streamlit.analise_df(df)
st.session_state['df1'] = df
