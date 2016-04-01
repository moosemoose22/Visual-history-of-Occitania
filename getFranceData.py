#!/usr/bin/python3

# Python 3!

import csv, time, urllib.request, urllib.parse, json, sys
france_cities_list = []

with open('outputFrance.csv', 'r') as data_file:
	reader = csv.reader(data_file)
	for row in reader:
		france_cities_list.append(row)

#    print data_file
#    writer = csv.writer(data_file, delimiter=',')
#    print writer
#    writer.writerows(france_cities_list)
#      france_cities_list.append(line.strip().split(','))

#with open('franceCities.csv', 'rb') as f:
#    reader = csv.reader(f)
#    france_cities_list = list(reader)

france_cities_list_smaller = list()
counter = 0
for i in france_cities_list:
	counter += 1
	g = [i[0], i[3], i[5], i[6]]
	france_cities_list_smaller.append(g)
	#{'lng': 0.107929, 'lat': 49.49437}

with open("outputFranceSmaller.csv", "w") as f:
	writer = csv.writer(f)
	writer.writerows(france_cities_list_smaller)

'''
arrPos = len(france_cities_list) - 1
print type(france_cities_list[arrPos][3])
print france_cities_list[arrPos][3]
response = urllib2.urlopen('http://nominatim.openstreetmap.org/search?q=' + france_cities_list[arrPos][3] + ',%20france&format=json')
franceData = response.read()
franceJSON = json.loads(franceData)
print franceJSON[0]['lon']
print franceJSON[0]['lat']
'''