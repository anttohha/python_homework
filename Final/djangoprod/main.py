s1=  [{'type': 'hotel-offers', 'hotel': {'type': 'hotel', 'hotelId': 'BWCDG714', 'chainCode': 'BW', 'dupeId': '700044772', 'name': 'Best Western Paris CDG Airport', 'cityCode': 'CDG', 'latitude': 49.00315, 'longitude': 2.52003}, 'available': True, 'offers': [{'id': 'WS9ING9XUX', 'checkInDate': '2023-10-01', 'checkOutDate': '2023-10-04', 'rateCode': 'AAA', 'rateFamilyEstimated': {'code': 'AAA', 'type': 'C'}, 'commission': {'percentage': '10'}, 'room': {'type': 'B1Q', 'typeEstimated': {'category': 'STANDARD_ROOM', 'beds': 1, 'bedType': 'QUEEN'}, 'description': {'text': 'AAA CAA RATE \n1 QUEEN BED,STANDARD\nSTANDARD', 'lang': 'EN'}}, 'guests': {'adults': 1}, 'price': {'currency': 'EUR', 'base': '310.50', 'total': '319.14', 'taxes': [{'code': 'TOTAL_TAX', 'amount': '8.64', 'currency': 'EUR', 'included': False}]}, 'policies': {'cancellations': [{'deadline': '2023-10-01T16:00:00+02:00'}], 'paymentType': 'guarantee'}, 'self': 'https://test.api.amadeus.com/v3/shopping/hotel-offers/WS9ING9XUX'}], 'self': 'https://test.api.amadeus.com/v3/shopping/hotel-offers?hotelIds=BWCDG714&adults=1&checkInDate=2023-10-01&checkOutDate=2023-10-04'}]

        # if len(hotels_by_city) > 0:
        #     print(f'название отеля- ', hotel_list[i]['name'])
        #     print(f'общая стоимость- ', hotels_by_city[0]['offers'][0]['price']['total'])
        #
        # time.sleep(1)



print(s1[0]['hotel']['latitude'])
print(s1[0]['hotel']['longitude'])