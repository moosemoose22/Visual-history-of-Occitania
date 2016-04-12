#!/usr/bin/python3

# Python 3!

import csv, time, urllib.request, urllib.parse, json, sys
spain_cities_list = []

with open('outputSpainWithLatLng.csv', 'r') as data_file:
	reader = csv.reader(data_file)
	for row in reader:
		spain_cities_list.append(row)

myDict = {}

counter = 0
for i in spain_cities_list:
	admin2name = i[3]
	rowIndex = myDict.get(admin2name, "Never")
	if (rowIndex == "Never"):
		myDict[admin2name] = counter
	else:
		rowObj = spain_cities_list[rowIndex]
		if (int(i[7]) > int(rowObj[7])):
			myDict[admin2name] = counter
	counter += 1

spain_cities_list_smaller = list()
counter = 0
for i in spain_cities_list:
	admin2name = i[3]
	if (myDict[admin2name] == counter):
		spain_cities_list_smaller.append(i)
	counter += 1
	#{'lng': 0.107929, 'lat': 49.49437}

with open("outputSpainFinal.csv", "w") as f:
	writer = csv.writer(f)
	writer.writerows(spain_cities_list_smaller)
