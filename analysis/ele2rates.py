# election count to rates

import csv

path = "../tables/"

sums = {}
with open("sums2010.csv") as fin:
    csvr = csv.reader(fin)
    for row in csvr:
        sums[row[0]] = row[1]

fieldnames = ["statistics_code","statistics_name","value","date","classification","county_code","county_name","country_code","country_name"]

with open(path + "cz_psp_2010_rates.csv","w") as fout:
    csvdw = csv.DictWriter(fout,fieldnames=fieldnames)
    csvdw.writeheader()
    with open(path + "cz_psp_2010.csv") as fin:
        csvdr = csv.DictReader(fin)
        for row in csvdr:
            r = row
            r['value'] = int(row['value']) / int(sums[row['county_code']])
            csvdw.writerow(row)
