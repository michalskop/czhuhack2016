# get the data into correct format

import csv
import slugify

name2name = {
    "Sum - VOLICI": "Non voters",
    "Sum - Česká strana sociálně demokratická": "ČSSD",
    "Sum - Strana svobodných občanů": "Svobodní",
    "Sum - Česká pirátská strana": "Piráti",
    "Sum - TOP 09": "TOP 09",
    "Sum - HLAVU VZHŮRU - volební blok": "Hlavu vzhůru",
    "Sum - Občanská demokratická strana": "ODS",
    "Sum - Romská demokratická strana": "RDS",
    "Sum - Klub angažovaných nestraníků": "KAN",
    "Sum - politické hnutí Změna": "Změna",
    "Sum - Strana soukromníků České republiky": "Soukromníci",
    "Sum - Křesťanská a demokratická unie - Československá strana lidová": "KDU-ČSL",
    "Sum - Pravý Blok": "PB",
    "Sum - Suverenita": "Suverenita",
    "Sum - Aktiv nezávislých občanů": "ANEO",
    "Sum - Strana Práv Občanů ZEMANOVCI": "SPOZ",
    "Sum - OBČANÉ 2011": "Občané 2011",
    "Sum - Úsvit přímé demokracie Tomia Okamury": "Úsvit",
    "Sum - Dělnická strana sociální spravedlnosti": "DSSS",
    "Sum - ANO 2011": "ANO",
    "Sum - LEV 21 - Národní socialisté": "LEV",
    "Sum - Strana zelených": "Zelení",
    "Sum - OBČANÉ.CZ": "Občané",
    "Sum - Liberálové.CZ": "Liberálové",
    "Sum - Věci veřejné": "VV",
    "Sum - Konzervativní strana": "KONS",
    "Sum - Komunistická str.Čech a Moravy": "KSČM",
    "Sum - Koruna Česká (monarch.strana)": "KČ",
    "Sum - Česká strana národně sociální": "ČSNS",
    "Sum - Česká str.sociálně demokrat.": "ČSSD",
    "Sum - NÁRODNÍ PROSPERITA": "NP",
    "Sum - Sdruž.pro rep.-Republ.str.Čsl.": "SPR-RSČ",
    "Sum - Moravané": "Moravané",
    "Sum - STOP": "STOP",
    "Sum - Strana Práv Občanů ZEMANOVCI": "SPOZ",
    "Sum - TOP 09": "TOP 09",
    "Sum - EVROPSKÝ STŘED": "ES",
    "Sum - Křesť.demokr.unie-Čs.str.lid.": "KDU-ČSL",
    "Sum - Volte Pr.Blok www.cibulka.net": "PB",
    "Sum - Česká str.národ.socialistická": "ČSNS",
    "Sum - Strana zelených": "Zelení",
    "Sum - Suverenita-blok J.Bobošíkové": "Suverenita",
    "Sum - Humanistická strana": "Humanisté",
    "Sum - Česká pirátská strana": "Piráti",
    "Sum - Dělnic.str.sociální spravedl.": "DSSS",
    "Sum - Strana svobodných občanů": "Svobodní",
    "Sum - Klíčové hnutí": "KH",
    "Sum - Občanská demokratická strana": "ODS",
    "Sum - Komunistická strana Čech a Moravy": "KSČM",
    "Sum - Koruna Česká": "KČ"

}

with open("psp2010.csv","w") as fout:
    csvw = csv.writer(fout)
    csvw.writerow(["statistics_code","statistics_name","value","date","classification","county_code","county_name","country_code","country_name"])
    with open("psp2010dev.csv") as fin:
        csvr = csv.reader(fin)
        for row in csvr:
            if not row[0] == "":
                county_name = row[0]
                county_code = slugify.slugify(county_name)
            statistics_code = slugify.slugify(name2name[row[1]])
            statistics_name = name2name[row[1]]
            r = [
                statistics_code,
                statistics_name,
                row[2],
                2010,
                "election",
                county_code,
                county_name,
                "cz",
                "Czechia"
            ]
            csvw.writerow(r)
