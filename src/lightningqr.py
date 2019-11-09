#!/usr/bin/python

from config import *
import requests, json, sys

### Pass the amount in EUR to this funtions to receive LNURL string back

def generate_lnurl(amt):

    request = requests.get(PRICEAPI)
    json_data = json.loads(request.text)
    price = json_data['last']

    satspereuro = round((1 / price) * 100000000)
    satamount = round(satspereuro * amt)

    print("Sats per Euro = " + str(satspereuro))
    print("Sats Total = " + str(satamount))


    #data = {
    #        'satoshis': str(round(amt)),
    #}

    #response = requests.post(
    #    APIURL,
    #    auth=(USER, PASS),
    #    data=json.dumps(data),
    #    )

    #response = json.loads(response.text)
    #print(response['lnurl'])

    response = json.dumps({'satoshis': satamount, 'lnurl': 'test'})


    print(response)

    #return json.dumps({'satoshis': satamount, 'lnurl': response['lnurl']})

    #{
   #'satoshis': satamount,
   #'lnurl': response['lnurl'],
   #}

if __name__ == '__main__':
    try:
        generate_lnurl(float(sys.argv[1]))
    except KeyboardInterrupt:
        sys.exit('Manually Interrupted')
