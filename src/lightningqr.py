#!/usr/bin/python

from config import *
import requests, json, sys

### Pass the amount in EUR to this funtion - receive satoshis and lnurl as json

def generate_lnurl(amt):
    request = requests.get(PRICEAPI)
    json_data = json.loads(request.text)
    price = json_data['last']

    satspereuro = round((1 / price) * 100000000)
    satamount = round(satspereuro * amt)

    print("Sats per Euro = " + str(satspereuro))
    print("Sats Total = " + str(satamount) + '\n')

    data = {
            'satoshis': str(round(amt)),
    }

    r = requests.post(
        APIURL,
        auth=(USER, PASS),
        data=json.dumps(data),
        )

    jsondata = json.loads(r.text)
    response = json.dumps({'satoshis': satamount, 'lnurl': jsondata['lnurl']})

    return response

if __name__ == '__main__':
    try:
        generate_lnurl(float(sys.argv[1]))
    except KeyboardInterrupt:
        sys.exit('Manually Interrupted')
