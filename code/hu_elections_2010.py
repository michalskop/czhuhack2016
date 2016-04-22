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

    lista_table = soup.find('p', text='Érvényes szavazatok száma:').find_next('table')
    rows = lista_table.find_all('tr')
    for row in rows[1:]:
        result = {}
        cells = row.find_all('td')
        result['part'] = cells[1].text
        result['szavazat'] = cells[2].text.replace(' ', '')
        result['percent'] = cells[3].text.replace('.', '')
        results.append(result)
    return results


def create_csv():
    keys = ['megye', 'part', 'szavazat', 'percent']
    writer = unicodecsv.DictWriter(sys.stdout, fieldnames=keys)
    writer.writeheader()
    data = get_all_megye()
    for megye in data.keys():
        results = get_parteredmenyek(data[megye])
        for result in results:
            result['megye'] = megye
            writer.writerow(result)


create_csv()
