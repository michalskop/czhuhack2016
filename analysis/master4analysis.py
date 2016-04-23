# select columns for analysis

import csv

path = "../tables/"

columns = [
    {
        "statistics_code": "unemployment",
        "classification": "unemployment",
        "date": "2013",
        "country_code": "cz"
    },
    {
        "statistics_code": "0-14",
        "classification": "age",
        "date": "2011",
        "country_code": "cz"
    },
    {
        "statistics_code": "65-",
        "classification": "age",
        "date": "2011",
        "country_code": "cz"
    },
    {
        "statistics_code": "no-education",
        "classification": "education",
        "date": "2011",
        "country_code": "cz"
    },
    {
        "statistics_code": "primary",
        "classification": "education",
        "date": "2011",
        "country_code": "cz"
    },
    {
        "statistics_code": "tertiary",
        "classification": "education",
        "date": "2011",
        "country_code": "cz"
    },
    {
        "statistics_code": "religious",
        "classification": "religion",
        "date": "2011",
        "country_code": "cz"
    }

]

fieldnames = ['county_code']
for c in columns:
    fieldnames.append(c['statistics_code'])

parties = {}
columns2 = {
    "classification": "election",
    "date": "2013"
}
with open("master.csv") as fin:
    csvdr = csv.DictReader(fin)
    for row in csvdr:
        ok = True
        for k in columns2:
            if not row[k] == columns2[k]:
                ok = False
        if ok:
            parties[row['statistics_code']] = row["statistics_code"]
for p in parties:
    fieldnames.append(p)

counties = {}
with open("master.csv") as fin:
    csvdr = csv.DictReader(fin)
    for row in csvdr:
        ok = True
        for k in columns2:
            if not row[k] == columns2[k]:
                ok = False
        if ok:
            counties[row['county_code']] = row["county_code"]


data = {}
for c in counties:
    data[c] = {}

with open("anal.csv","w") as fout:
    csvdw = csv.DictWriter(fout,fieldnames=fieldnames)
    csvdw.writeheader()
    with open("master.csv") as fin:
        csvdr = csv.DictReader(fin)
        for row in csvdr:
            for c in columns:
                ok = True
                for k in c:
                    if not c[k] == row[k]:
                        ok = False
                if ok:
                    data[row['county_code']][row['statistics_code']] = row['value']
                    data[row['county_code']]['county_code'] = row['county_code']

    with open("master.csv") as fin:
        csvdr = csv.DictReader(fin)
        for row in csvdr:
            ok = True
            for k in columns2:
                if not row[k] == columns2[k]:
                    ok = False
            if ok:
                data[row['county_code']][row['statistics_code']] = row["value"]

with open("data.csv","w") as fout:
    csvdw = csv.DictWriter(fout,fieldnames=fieldnames)
    csvdw.writeheader()
    for k in data:
        csvdw.writerow(data[k])
