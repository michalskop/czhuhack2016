#coding: utf-8

import requests
import unicodecsv
from slugify import slugify
import constants as m
import sys
from bs4 import BeautifulSoup


def build_url(megye, telepules, szavazokor):
    return 'http://www.valasztas.hu/dyn/pv14/szavossz/hu/M{:02d}/T{:03d}/szkjkv_{:03d}.html'.format(megye, telepules, szavazokor)
 
 
def get_page(megye, telepules, szavazokor):
    url = build_url(megye, telepules, szavazokor)
    page = requests.get(url)
    if page.status_code == requests.codes.ok:
        return page.content
 
 
def get_all_szavazokor(megye, telepules):
    '''
   Returns a dictionary of pages.
   key = szavazokor
   value = text of html
   '''
    data = {}
    szavazokor = 1
    while True:
        document = get_page(megye, telepules, szavazokor)
        if not document:
            break
        data[szavazokor] = document
        szavazokor += 1
    return data


def get_all_telepules(megye):
    data = {}
    telepules = 1
    while True:
        document = get_all_szavazokor(megye, telepules)
        if not document:
            break
        data[telepules] = document
        telepules += 1
    return data
 

def get_all_megye():
    data = {}
    megye = 1
    while megye < 21:
        data[megye] = get_all_telepules(megye)
        megye += 1
    return data


"""
adatszerkezet:
{megye: {telepules: {szavazokor:html}, telepules: {szavazokor:html},..}, telepules: {}, megye:{}}

"""


def jegyzekben_megjelent(content):
    soup = BeautifulSoup(content)
    jegyzokonyv = soup.find(text='Jegyzőkönyv')
    voter_table = jegyzokonyv.find_next('table')

    voter_data = voter_table.find_all('td')
    total = voter_data[0].text
    voters = list(voter_data[1])
    non_voters = int(total) - int(voters[0])

    nonvoter = dict()
    nonvoter['statistics_code'] = 'non-voters'
    nonvoter['statistics_name'] = 'Non voters'
    nonvoter['value'] = non_voters

    return nonvoter


#content = get_page(1, 1, 1)
#print jegyzekben_megjelent(content)


def get_parteredmenyek(content):
    results = list()
    soup = BeautifulSoup(content, from_encoding='utf-8')
    soup.prettify(formatter=lambda s: s.replace(u'\xa0', ' '))
    jegyzokonyv = soup.find(text='Jegyzőkönyv')
    voter_table = jegyzokonyv.find_next('table')

    voter_data = voter_table.find_all('td')
    total = voter_data[0].text
    voters = list(voter_data[1])
    #non_voters = int(total) - int(voters[0].replace(' ', ''))
    non_voters = 0

    nonvoter = dict()
    nonvoter['statistics_code'] = 'non-voters'
    nonvoter['statistics_name'] = 'Non voters'
    nonvoter['value'] = non_voters
    results.append(nonvoter)

    jelolt_table = soup.find('p', text='A szavazatok száma pártlistánként').find_next('table')
    #print type(jelolt_table)

    rows = jelolt_table.find_all('tr')
    #print 'rows: ', rows
    for row in rows[1:]:
        party = dict()
        cells = row.find_all('td')
        #print 'cells: ', cells
        party['statistics_code'] = slugify(cells[1].text)
        party['statistics_name'] = cells[1].text
        party['value'] = cells[2].text
        results.append(party)

    return results


def create_csv():

    keys = ['county_code', 'county_name', 'classification', 'date', 'country_code', 'country_name', 'value', 'statistics_code', 'statistics_name']

    writer = unicodecsv.DictWriter(sys.stdout, fieldnames=keys)

    writer.writeheader()
    data = get_all_megye()
    for megye in data.keys():
        for telepules in data[megye].keys():
            for szavazokor in data[megye][telepules].keys():
                #if data[megye][telepules][szavazokor] is not None:
                results = get_parteredmenyek(data[megye][telepules][szavazokor])
                #results = jegyzekben_megjelent(data[megye][telepules][szavazor])
                for result in results:
                    result['county_code'] = slugify(m.COUNTIES[megye])
                    result['county_name'] = m.COUNTIES[megye]
                    result['classification'] = 'election'
                    result['date'] = 2014
                    result['country_code'] = 'hu'
                    result['country_name'] = 'Hungary'

                    #result['telepules'] = telepules
                    #result['szavazokor'] = szavazokor
                    writer.writerow(result)


create_csv()
