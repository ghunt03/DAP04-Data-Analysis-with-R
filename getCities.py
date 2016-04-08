import csv
import sys
import codecs
import pprint
csv.field_size_limit(sys.maxsize)

tag_keys = {}

suburb_maps = {
    "ANNADALE": "ANNANDALE",
    "AMERST": "AMHERST",
 	"ANNANDALE ON HUDSON": "ANNANDALE",
 	"":"NEW YORK",
 	"21 CAMELOT LANE":"SETAUKET",
 	"APO.  AE":"NEW YORK",
 	"ARDSLEY ON HUDSON": "ARDSLEY",
 	"BAYSIDE HILLS": "BAYSIDE",
 	"BEDFORD CORNER":"BEDFORD CORNERS",
 	'BELLEROSE MANOR': 'BELLEROSE',
 	'BOLTON LNDG': 'BOLTON LANDING',
 	'BRIARCLIFF': 'BRIARCLIFF MANOR',
 	'BRIDGE LAMPTON': 'BRIDGEHAMPTON',
 	'BRIDGEHAMPTON, NY. 11932': 'BRIDGEHAMPTON',
 	'BROOKLN': 'BROOKLYN',
 	'BROOKLYN HGTS': 'BROOKLYN HEIGHTS',
 }

def addToKeyCheck(value, cities):
	if not value in cities:
		value = "_"+value
	if value in tag_keys:
		tag_keys[value] = tag_keys[value] + 1
	else:
		tag_keys[value] = 1

def update_suburb_name(suburb_name):
    suburb_name = suburb_name.upper()
    if suburb_name in suburb_maps:
        suburb_name = suburb_maps[suburb_name]
    return suburb_name



def createCities():
	data = []
	with open("US.txt", "rb") as f:
	    reader = csv.reader(f, delimiter="\t")
	    rows = list(reader)
	    for row in rows:
			if row[10] == "NY":
				city_name = update_suburb_name(row[1])
				item = [city_name, row[4], row[5]]
				data.append(item)

	file_out = "cities.csv"
	with codecs.open(file_out, "w") as fo:
		writer = csv.writer(fo)
		writer.writerow(['city','latitude','longitude'])
		writer.writerows(data)

def getCities():
	data = []
	with open("US.txt", "rb") as f:
	    reader = csv.reader(f, delimiter="\t")
	    rows = list(reader)
	    for row in rows:
			if row[10] == "NY":
				city_name = update_suburb_name(row[1])
				data.append(city_name)
	return data

def audit(filename, cityCol, cities):
	with open(filename, "rU") as f:
		reader = csv.reader(f, delimiter="\t")
		rows = list(reader)
		for row in rows:
			city_name = update_suburb_name(row[cityCol])
			addToKeyCheck(city_name, cities)
	



if __name__ == '__main__':
	#cities = getCities()
	#audit("P00000001-NY.txt",4, cities)
	createCities()
	pprint.pprint(tag_keys)
