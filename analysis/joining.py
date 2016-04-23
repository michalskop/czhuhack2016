# join tables

import csv

path = "../tables/"

files = [
    "cz_ages_2011",
    "cz_psp_2010_rates",
    "cz_psp_2013_rates",
    "cz_unemployment_2010",
    "cz_unemployment_2013",
    "hu_unemployment_2010",
    "hu_unemployment_2014",
    "cz_education_2011",
    "cz_religion_2011",
    "hu_votes_2010_v2",
    "hu_age_2010_v2",
    "hu_education_2011_v2"
]

fieldnames = ["statistics_code","statistics_name","value","date","classification","county_code","county_name","country_code","country_name"]

with open("master.csv","w") as fout:
    csvdw = csv.DictWriter(fout,fieldnames=fieldnames)
    csvdw.writeheader()
    for f in files:
        with open(path + f + ".csv") as fin:
            csvdr = csv.DictReader(fin)
            for row in csvdr:
                csvdw.writerow(row)
