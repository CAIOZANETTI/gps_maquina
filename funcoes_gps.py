import math

def haversine_distance(lat1:float, lon1:float, lat2:float, lon2:float,testar:bool)->float:
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
	if testar ==True:
		lat1 = 52.5200  # Berlin, Germany
		lon1 = 13.4050
		lat2 = 48.8566  # Paris, France
		lon2 = 2.3522

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
	distance = earth_radius * c
	
	return distance
