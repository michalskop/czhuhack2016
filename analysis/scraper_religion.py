# scraper education

import csv
import requests
from lxml import html
import copy
import slugify

with open("cz_religion_2011.csv","w") as fout:
    fieldnames = ["statistics_code","statistics_name","value","date","classification","county_code","county_name","country_code","country_name"]
    csvdw = csv.DictWriter(fout,fieldnames=fieldnames)
    csvdw.writeheader()
    with open("cz_counties.csv") as fin:
        csvr = csv.reader(fin)
        for row in csvr:
            url =             "https://vdb.czso.cz/vdbvo2/faces/cs/embeded.jsf?page=profil-uzemi&ewr=false&rn=N&rp=true&rz=true&u=__VUZEMI__101__" + row[0] + "&pvo=PU-SLDB-5&z=T&f=TABULKA&clsp=31310&zo=A&rqup=A"

            r = requests.get(url)
            domtree = html.fromstring(r.content)

            trs = domtree.xpath('//table/tr');
            rs = []
            for i in range (3,6):
                tds = trs[i].xpath('td')
                rs.append(int(trs[i].xpath('td/span')[len(tds)-3].text.replace('\xa0','')))

            county_name = row[1]
            county_code = slugify.slugify(county_name)

            r = {
                'statistics_code': 'religious',
                'statistics_name': 'Religious',
                'value': rs[2]/rs[0],
                'date': 2011,
                'classification': "religion",
                'county_code': county_code,
                'county_name': county_name,
                'country_code': "cz",
                'country_name': "Czechia"
            }
            csvdw.writerow(r)

            # raise(Exception)

            print(county_code)
