#!/usr/bin/python3

# Python 3!

import csv, time, urllib.request, urllib.parse, json, sys
spain_cities_list = []

with open('outputSpainIne.csv', 'r') as data_file:
	reader = csv.reader(data_file)
	for row in reader:
		spain_cities_list.append(row)

counter = 0
baseURL = "https://maps.googleapis.com/maps/api/geocode/json?address="
endURL = ",%20spain&key=AIzaSyBJQ24b0wcXyskkuYWcX9dpt-1rP4lY2AQ"
for i in spain_cities_list:
	counter += 1
	if ((counter % 8) == 0):
		time.sleep(1.5)
	myUrl = baseURL + urllib.parse.quote(i[1]) + endURL
	print (myUrl)

	response = urllib.request.urlopen(myUrl)
	#data = json.load(response)
	data = json.loads(response.read().decode(response.info().get_param('charset') or 'utf-8'))

	if (data["status"] == "OK"):
		myData = data["results"][0]["geometry"]["location"]
		myRegionName = myAdmin3Name = ''
		for googleAddrItem in data["results"][0]["address_components"]:
			if ((googleAddrItem["types"][0] == "administrative_area_level_1" or googleAddrItem["types"][0] == "colloquial_area")):
				myRegionName = googleAddrItem["long_name"]

			if (googleAddrItem["types"][0] == "administrative_area_level_3"):
				myAdmin3Name = googleAddrItem["long_name"]

		i.insert(0, myRegionName)
		i.insert(2, myAdmin3Name)
		
		i.extend([myData['lat'], myData['lng']])
		print (i[3])
	else:
		print (i[0] + " " + i[1] + " missing")
	#{'lng': 0.107929, 'lat': 49.49437}

with open("outputNewSpainIneWithLatLng.csv", "w") as f:
	writer = csv.writer(f)
	writer.writerows(spain_cities_list)