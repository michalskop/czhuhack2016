# transpose the age groups

import csv
import slugify

with open("cz_ages_2010.csv","w") as fout:
    csvw = csv.writer(fout)
    csvw.writerow(["statistics_code","statistics_name","value","date","classification","county_code","county_name","country_code","country_name"])
    with open("ages2010dev.csv") as fin:
        csvr = csv.reader(fin)
        for row in csvr:
            statistics_code = "0-14"
            statistics_name = "0-14"
            value = row[7]
            r = [
                statistics_code,
                statistics_name,
                value,
                2011,
                "age",
                slugify.slugify(row[0]),
                row[0],
                "cz",
                "Czechia"
            ]
            csvw.writerow(r)
            statistics_code = "15-64"
            statistics_name = "15-64"
            value = row[8]
            r = [
                statistics_code,
                statistics_name,
                value,
                2011,
                "age",
                slugify.slugify(row[0]),
                row[0],
                "cz",
                "Czechia"
            ]
            csvw.writerow(r)
            statistics_code = "65-"
            statistics_name = "65-"
            value = row[9]
            r = [
                statistics_code,
                statistics_name,
                value,
                2011,
                "age",
                slugify.slugify(row[0]),
                row[0],
                "cz",
                "Czechia"
            ]
            csvw.writerow(r)
