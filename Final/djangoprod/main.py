a1 = {'type': 'flight-offer', 'id': '1', 'source': 'GDS', 'instantTicketingRequired': False, 'nonHomogeneous': False,
      'oneWay': False, 'lastTicketingDate': '2023-08-08', 'lastTicketingDateTime': '2023-08-08',
      'numberOfBookableSeats': 1, 'itineraries': [{'duration': 'PT8H15M', 'segments': [
        {'departure': {'iataCode': 'CDG', 'terminal': '1', 'at': '2023-08-08T13:55:00'},
         'arrival': {'iataCode': 'ATH', 'at': '2023-08-08T18:05:00'}, 'carrierCode': 'A3', 'number': '617',
         'aircraft': {'code': '320'}, 'operating': {'carrierCode': 'A3'}, 'duration': 'PT3H10M', 'id': '98',
         'numberOfStops': 0, 'blacklistedInEU': False}, {'departure': {'iataCode': 'ATH', 'at': '2023-08-08T19:15:00'},
                                                         'arrival': {'iataCode': 'LHR', 'terminal': '2',
                                                                     'at': '2023-08-08T21:10:00'}, 'carrierCode': 'A3',
                                                         'number': '608', 'aircraft': {'code': '32Q'},
                                                         'operating': {'carrierCode': 'A3'}, 'duration': 'PT3H55M',
                                                         'id': '99', 'numberOfStops': 0, 'blacklistedInEU': False}]}],
      'price': {'currency': 'EUR', 'total': '105.58', 'base': '30.00',
                'fees': [{'amount': '0.00', 'type': 'SUPPLIER'}, {'amount': '0.00', 'type': 'TICKETING'}],
                'grandTotal': '105.58', 'additionalServices': [{'amount': '43.00', 'type': 'CHECKED_BAGS'}]},
      'pricingOptions': {'fareType': ['PUBLISHED'], 'includedCheckedBagsOnly': False}, 'validatingAirlineCodes': ['A3'],
      'travelerPricings': [{'travelerId': '1', 'fareOption': 'STANDARD', 'travelerType': 'ADULT',
                            'price': {'currency': 'EUR', 'total': '105.58', 'base': '30.00'}, 'fareDetailsBySegment': [
              {'segmentId': '98', 'cabin': 'ECONOMY', 'fareBasis': 'PNFLXLC', 'brandedFare': 'FLEX', 'class': 'P',
               'includedCheckedBags': {'quantity': 0}},
              {'segmentId': '99', 'cabin': 'ECONOMY', 'fareBasis': 'PNFLXLC', 'brandedFare': 'FLEX', 'class': 'P',
               'includedCheckedBags': {'quantity': 0}}]}]}

datain = a1['itineraries'][0]['segments'][0]['departure']['at']
terminalin = a1['itineraries'][0]['segments'][0]['departure']['terminal']
dataout = a1['itineraries'][0]['segments'][0]['arrival']['at']
corridorin = a1['itineraries'][0]['segments'][0]['carrierCode']
aircraft = a1['itineraries'][0]['segments'][0]['aircraft']['code']
datain1 = datain[0: 10]
time1 = datain[11:19]
dataout2 = dataout[0:10]
timeout2 = dataout[11:19]

terminalout = a1['price']
typemoney = a1['price']['currency']
allmonet = a1['price']['total']
aircraftNumber = a1['itineraries'][0]['segments'][1]['arrival']['terminal']

print(aircraftNumber)