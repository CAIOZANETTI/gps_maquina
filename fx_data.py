import math
import pandas as pd


def analise_dataframe(df:pd.DataFrame)->dict:
	"""
	Mostrar uma analise do conteudo do dataframe
	"""
	dic = {}
	if df.isna().sum().sum()==0:
		dic['nulo'] = 'sem valores nulos'
	else:
		dic['nulo'] = df.isna().sum()

	dic['duplicados'] = df.duplicated().sum()
	dic['tipo_dados'] = df.dtypes
	dic['objetos'] = df.select_dtypes(include=['object']).columns

	return dic

def df_filtrar_datas(df:pd.DataFrame,inicio,fim)->pd.DataFrame:
	#todo: finalizar... não fiz por preguiça...
	# testar a condição de data primento.... 
	st.text('disponivel: jan/2022 -> ago/2022')
	cols = st.columns([1,1])
	cols[0].date_input('inicio',datetime.datetime(2022,1,1),key='inicio')
	cols[1].date_input('fim',datetime.datetime(2022,1,8),key='fim')

	dias = st.session_state['fim'] - st.session_state['inicio']
	dias = dias.days

	if dias>0:
		cols = st.columns([1,1])
		cols[0].info('Periodo: '+str(dias)+' dias')
		desativo=False

	elif dias<0:
		cols[0].warning('NEGATIVO REVISAR '+str(dias)+' dias')
		desativo=True


	df['data'] = df['data_hora'].dt.date
	df1 = df[(df['data']>= inicio) & (df['data']<= fim)]
	return df1

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
	obter coluna: hora, nome_dia,lat_lon
	"""
	df['data_hora'] = pd.to_datetime(df['data_hora'], format='%m/%d/%Y %H:%M:%S')
	df['data'] = df['data_hora'].dt.date
	df['hora'] = df['data_hora'].dt.hour
	df['minuto']= df['data_hora'].dt.minute
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
	df['motor_ligado'] = df['motor_ligado'].astype(bool)


	#fitrar dados remover linhas
	atividades_remover = ['primeiro_acerto_do_gps', 'gsm_metrics-pt','gsm_diagnostics-pt']
	df = df[~df['atividade'].isin(atividades_remover)]

	#converter colunas object to string
	df = df.astype({'nome_dia': 'string','lat_lon':'string','atividade':'string'})


	#remover colunas
	for coluna in remover_colunas:
		if coluna in df.columns:
			df = df.drop(coluna,axis=1)
	return df

def count_weed_by_name(start:str, end:str) -> pd.DataFrame:
	"""
	start_date = '2022-01-01'
	end_date = '2022-08-01'
	"""

	serie = pd.date_range(start, end)
	serie = serie.day_name().str.lower()
	serie = serie.value_counts()

	order = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
	serie = serie.reindex(order)
	df = pd.DataFrame({'qtd':serie})
	df.rename_axis('nome_dia', inplace=True)
	
	return df

def df_count_query_merge(df:pd.DataFrame,coluna:str,ordem_index=list,querys:dict)->pd.DataFrame:
	i=0
	for nome,query in querys.items():
		if i==0:
			df1 = df.query(query)
			df1 = df1[coluna].value_counts().reset_index()
			df1.columns=['nome_dia',nome]
		else:
			df2 = df.query(query)
			df2 = df2[coluna].value_counts().reset_index()
			df2.columns=['nome_dia',nome]
			df3 = pd.merge(df2,df1,on='nome_dia',how='outer')
			df1=df3
		i+=1

	df3.set_index(coluna,inplace=True)
	df3 = df3.reindex(index=ordem_index)
	
	return df3
