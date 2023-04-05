import json
import sys

def countshoping():
    with open('shop.json') as f:
        jsodict = json.load(f)
        sum1 = 0
        for i in jsodict:
            sum1 += int(jsodict[i])

        print(f"\n сумма покупок {sum1} ")


def writeinjson(shopdict):
    testjson1 = json.dumps(shopdict)
    with open("shop.json", "a") as my_file:
        my_file.write(testjson1)


shoping = {}
while (True):
    nameshop1 = input('name shoping = ')
    if nameshop1 == 'стоп':
        writeinjson(shoping)
        countshoping()
        sys.exit()
    else:
        priceshop1 = int(input('price shop = '))
        shoping[nameshop1] = priceshop1
