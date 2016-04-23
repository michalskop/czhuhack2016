#coding: utf-8

import requests
import unicodecsv
from slugify import slugify
import sys
import constants as m
from bs4 import BeautifulSoup


def build_url(megye):
    return 'http://valasztas.hu/dyn/pv10/outroot/vdin1/hu/ljk{:02d}.htm'.format(megye)


def get_page(megye):
    url = build_url(megye)
    page = requests.get(url)
    if page.status_code == requests.codes.ok:
        return page.content


def get_all_megye():
    data = {}
    for i in range(1, 21):
        document = get_page(i)
        data[i] = document
    return data


def get_parteredmenyek(content):
    results = list()
    soup = BeautifulSoup(content)

    registry_table = soup.find('p', text='a) A választók nyilvántartása').find_next('table')
    row = registry_table.find_all('tr')[3]
    total = row.find_all('td')[4].text.replace(' ', '')

    voter_table = registry_table.find_next('table')
    row = voter_table.find_all('tr')[3]
    #voters = row.find_all('td')[4].text.replace(' ', '')

    #non_voters = int(total) - int(voters[0].replace(' ', ''))
    non_voters = 0
    nonvoter = dict()
    nonvoter['statistics_code'] = 'non-voters'
    nonvoter['statistics_name'] = 'Non voters'
    nonvoter['value'] = non_voters
    results.append(nonvoter)

    lista_table = soup.find('p', text='Érvényes szavazatok száma:').find_next('table')
    rows = lista_table.find_all('tr')
    for row in rows[1:]:
        result = {}
        cells = row.find_all('td')
        result['statistics_code'] = slugify(cells[1].text)
        result['statistics_name'] = cells[1].text
        result['value'] = cells[2].text.replace(' ', '')
        #result['percent'] = cells[3].text.replace('.', '')
        results.append(result)

    return results


def create_csv():
    keys = ['county_code', 'county_name', 'classification', 'date', 'country_code', 'country_name', 'value', 'statistics_code', 'statistics_name']
    writer = unicodecsv.DictWriter(sys.stdout, fieldnames=keys)
    writer.writeheader()
    data = get_all_megye()
    for megye in data.keys():
        results = get_parteredmenyek(data[megye])
        for result in results:
            result['county_code'] = slugify(m.COUNTIES[megye])
            result['county_name'] = m.COUNTIES[megye]
            result['classification'] = 'election'
            result['date'] = 2010
            result['country_code'] = 'hu'
            result['country_name'] = 'Hungary'
            writer.writerow(result)


create_csv()
