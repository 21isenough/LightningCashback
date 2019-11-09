#!/usr/bin/python

### Pass the amount in EUR to this funtions to receive LNURL string back

def generate_lnurl(amt):

    request = requests.get('https://apiv2.bitcoinaverage.com/indices/global/ticker/BTCEUR')
    json_data = json.loads(request.text)
    price = json_data['last']

    print(price)

    data = {
            'satoshis': str(round(amt)),
    }

    response = requests.post(
        APIURL,
        auth=(USER, PASS),
        data=json.dumps(data),
        )

    response = json.loads(response.text)
    print(response['lnurl'])
