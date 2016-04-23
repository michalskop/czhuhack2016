# -*- coding: utf-8 -*-

# geocoding using open street map (centers)
# http://wiki.openstreetmap.org/wiki/Nominatim

import csv
import requests
import json
import slugify

fieldnames = [
    "id","latitude","longitude","name"
]
with open("geocoded.csv","w") as fout:
    csvdw = csv.DictWriter(fout,fieldnames=fieldnames)
    csvdw.writeheader()
    with open("counties.csv") as fin:
        csvr = csv.reader(fin)
        for row in csvr:
            url = "http://nominatim.openstreetmap.org/search?countrycodes=" + row[1] + "&format=json&county=" + row[0]
            r = requests.get(url)
            djson = json.loads(r.text)
            rnew = {
                "id": slugify.slugify(row[0]),
                "name": row[0]
            }
            if len(djson) > 0:
                rnew['latitude'] = djson[0]['lat']
                rnew['longitude'] = djson[0]['lon']
            else:
                url = "http://nominatim.openstreetmap.org/search?countrycodes=" + row[1] + "&format=json&city=" + row[0]
                r = requests.get(url)
                djson = json.loads(r.text)
                if len(djson) > 0:
                    rnew['latitude'] = djson[0]['lat']
                    rnew['longitude'] = djson[0]['lon']

            csvdw.writerow(rnew)
            print(rnew)
