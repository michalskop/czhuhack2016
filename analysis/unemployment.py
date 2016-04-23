# reorder unemployment

import csv
import slugify

with open("cz_unemployment_2013.csv","w") as fout:
    csvw = csv.writer(fout)
    csvw.writerow(["statistics_code","statistics_name","value","date","classification","county_code","county_name","country_code","country_name"])
    with open("czUnemploymentPercent.raw.csv") as fin:
        csvr = csv.reader(fin)
        for row in csvr:
            statistics_code = "unemployment"
            statistics_name = "Unemployment"
            r = [
                statistics_code,
                statistics_name,
                row[2],
                2013,
                "unemployment",
                slugify.slugify(row[0]),
                row[0],
                "cz",
                "Czechia"
            ]
            csvw.writerow(r)
