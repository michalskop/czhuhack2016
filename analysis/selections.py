#selecting the counties

parties = [
    {
        "party": "cssd",
        'selections':[
            {
                "statistics_code": "tertiary",
                "coef": -0.15,
                "sign": -1
            },
            {
                "statistics_code": "religious",
                "coef": 0.2,
                "sign": 1
            },
        ]
    },
# kscm
    {
        "party":"kscm",
        'selections': [{
            "statistics_code": "tertiary",
            "coef": -0.3,
            "sign": -1
        }]
    },
# top 09
    {
        "party": "top-09",
        'selections': [
            {
                "statistics_code": "religious",
                "coef": -0.23,
                "sign": -1
            },
            {
                "statistics_code": "0-14",
                "coef": 0.1,
                "sign": 1
            }
        ]
    },
    {
        "party": "ano",
        'selections': [
            {
                "statistics_code": "0-14",
                "coef": 0.05,
                "sign": 1
            },
            {
                "statistics_code": "primary",
                "coef": -0.1,
                "sign": -1
            }
        ]
    },
    {
        "party": "kdu-csl",
        'selections': [
            {
                "statistics_code": "religious",
                "coef": 0.1,
                "sign": 1
            },
            {
                "statistics_code": "65-",
                "coef": 0.1,
                "sign": 1
            }
        ]
    }
]

averages = {}
sums = {}
i = 0
with open("data_cz.csv") as fin:
    csvdr = csv.DictReader(fin)
    for row in csvdr:
        for k in row:
            if not k == 'county_code':
                try:
                    sums[k]
                except:
                    sums[k] = 0
                sums[k] += float(row[k])
        i += 1
    for k in row:
        if not k == 'county_code':
            averages[k] = sums[k]/i

data ={}
fieldnames = ['county_code']
for p in parties:
    fieldnames.append(p['party'])
for p in parties:
    # strongholds
    party = p['party']
    strongholds = []
    with open("data_cz.csv") as fin:
        csvdr = csv.DictReader(fin)
        for row in csvdr:

            try:
                data[row['county_code']]
            except:
                data[row['county_code']] = {"county_code":row['county_code']}

            if float(row[party]) >= 1.25*averages[party]:
                data[row['county_code']][party] = 1
                print(row['county_code'])
            else:
                ok = True
                for s in selections:
                    val = float(row[s['statistics_code']])
                    stdval = (val - averages[s['statistics_code']])/averages[s['statistics_code']]
                    print(stdval)
                    if s['sign'] == 1:
                        if stdval < s['coef']:
                            ok = False
                    else:
                        if stdval > s['coef']:
                            ok = False
                if ok:
                    data[row['county_code']][party] = -1
                    print(row['county_code'])
                else:
                    data[row['county_code']][party] = 0

with open("strongs.csv","w") as fout:
    csvdw = csv.DictWriter(fout,fieldnames=fieldnames)
    csvdw.writeheader()
    for k in data:
        csvdw.writerow(data[k])

# with open("strongs.csv","w") as fout:
#     csvw = csv.writer(fout)
#     for row in strongholds:
#         csvw.writerow(row)
