import requests
from requests import request
import time
from bs4 import BeautifulSoup
import re
import json
import csv
from operator import itemgetter


def copyhtml():
    for i in range(1, 7):
        url = f'https://cars.av.by/filter?brands[0][brand]=8&brands[0][model]=5865&brands[0][generation]=4441&page={i}'

        html_text = requests.get(url).text
        print(html_text)
        with open(f'bmw{i}.html', 'w', encoding='utf-8') as f:
            f.write(html_text)
            f.close()


def createmassiv():
    links = []
    pricerubles = []
    pricebaks = []
    godvips = []
    volums = []
    tipdvigki = []
    probegbmw = []
    avby2 = []
    i = 1
    while i != 7:
        with open(f"bmw{i}.html") as file:
            src = file.read()
            soup = BeautifulSoup(src, "lxml")
            link_car = soup.find_all("a", class_="listing-item__link")
            price = soup.find_all("div", class_="listing-item__price")
            price2 = soup.find_all("div", class_="listing-item__priceusd")
            car_dvigun = soup.find_all("div", class_="listing-item__params")
            for linkscars in link_car:
                link_pages = linkscars.get('href')
                links.append(link_pages)
            for pricecar in price:
                str1 = str(pricecar)
                str1 = str1[33:39]
                str1 = str1.split()
                str2 = str1[0] + str1[1]
                pricecarinrubl = int(str2)
                pricerubles.append(pricecarinrubl)
            for pricedol in price2:
                text = str(pricedol)
                strdol = re.search(r'>(.+?)<', text).group(1)
                strdol = strdol[1:-1:]
                strdol = strdol.split()
                strdol = strdol[0] + strdol[1]
                pricebaks.append(int(strdol))
            for dviguni in car_dvigun:
                text2 = str(dviguni)
                godvip = re.search(r'div>(.+?)</div', text2).group(1)
                godvipstr = str(godvip)
                godvipstr = godvipstr[:-3]
                godvips.append(int(godvipstr))
                volume1 = text2.split()
                volume1 = volume1[5]
                volume1 = volume1[3:]
                volums.append(float(volume1))
                tipdviguna = text2.split()
                tipdviguna = tipdviguna[9]
                tipdviguna = tipdviguna[3:-4]
                tipdvigki.append(tipdviguna)
                probeg = re.search(r'span>(.+?)</span', text2).group(1)
                probeg = probeg.split()
                probeg = probeg[0] + probeg[1]
                probegbmw.append(int(probeg))
        i += 1

    for elem2 in range(len(links)):
        avby2.append(
            [links[elem2], pricerubles[elem2], godvips[elem2], volums[elem2], tipdvigki[elem2],
             probegbmw[elem2]])

    for slov in avby2:
        avby = dict.fromkeys(pricebaks, slov)

    sortavby = dict(sorted(avby.items(), key=lambda item: item[0]))
    data_dict = []
    data_dict.append(sortavby)
    with open('data.json', 'w', encoding='utf8') as json_file:
        json.dump(data_dict, json_file, indent=4)

    with open('data.csv', 'w', newline='') as csv_file:
        writer=csv.writer(csv_file)
        writer.writerow(data_dict)


    print(sortavby)


createmassiv()
