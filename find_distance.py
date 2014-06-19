import urllib, json, numpy, time 
 
def convert(input):
    if isinstance(input, dict):
        return {convert(key): convert(value) for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [convert(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

def get_distance(from_loc, to_loc):
	# Mapquest API Key 
	my_key = "Fmjtd%7Cluur2gu7lu%2Cal%3Do5-9azl9y"
	from_location = str(from_loc) 
	to_location = str(to_loc)
	url = "https://www.mapquestapi.com/directions/v2/route?key="+my_key+"&ambiguities=ignore&avoidTimedConditions=false&doReverseGeocode=true&outFormat=json&routeType=fastest&timeType=1&enhancedNarrative=false&shapeFormat=raw&generalize=0&locale=en_US&unit=m&from="+from_location+"&to="+to_location+"&drivingStyle=2&highwayEfficiency=21.0"
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	data = convert(data)
	distance =  data["route"]["distance"]
	a = data["route"]["locations"]
	postalcode = []
	coordinates = []
	for post in a:
		postalcode.append(post["postalCode"])
		coordinates.append(post["displayLatLng"])
	return postalcode[0], distance, coordinates[0]	


# Read in the Names of Restaurants and their address: 
restaurant_data = numpy.genfromtxt("restaurant_database.csv", dtype = None, names = "restaurant_name, rest_address", usecols=(0,2), skip_header=1, delimiter = ",")
restaurant_name = restaurant_data["restaurant_name"]
rest_address    = restaurant_data["rest_address"]

#Run the Maps API and get the distances:
filename = open("restaurant_distances_94501.csv", "w")
filename.write("Name, Address, Zipcode, Distance_from_94501, lat, lng \n") 
for j in range(len(rest_address)):
	this_address  = rest_address[j]
	this_restName = restaurant_name[j]

	# Initializing the from address:  
	from_address = ""
	for i in range(0, len(this_address)):
		if this_address[i] == " ":
			from_address = from_address + "+"
		else:
			from_address = from_address + this_address[i]

	#print from_address 	
	my_dist = get_distance(from_address, 94501)
	my_zipcode = my_dist[0]
	my_distance = my_dist[1]
	my_lat = my_dist[2]["lat"]
	my_lng = my_dist[2]["lng"]
	filename.write("{this_restName:5s}, {this_address:5s}, {my_zipcode:.5s}, {my_distance:.3f}, {my_lat:.5f}, {my_lng:5f}\n".format(this_restName=this_restName, this_address=this_address, my_zipcode=my_zipcode, my_distance=my_distance, my_lat = my_lat, my_lng=my_lng)) 

filename.close()