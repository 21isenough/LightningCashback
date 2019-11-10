from flask import Flask, jsonify, request, send_from_directory
# from escpos.printer import Usb

import requests, json, sys, os

from config import *

app = Flask(__name__)

@app.route('/lnurl', methods=['POST'])
def generate_lnurl():
    request_data = request.get_json()

    #p = Usb(0x0483, 0x5720, 0)

    price_request = requests.get(PRICEAPI)
    price_json = json.loads(price_request.text)
    price = price_json['last']

    satspereuro = round((1 / price) * 100000000)
    satamount = round(satspereuro * float(request_data['euro']))

    print("Sats per Euro = " + str(satspereuro))
    print("Sats Total = " + str(satamount) + '\n')

    data = {
            'satoshis': str(round(satamount)),
    }

    r = requests.post(
        APIURL,
        auth=(USER, PASS),
        data=json.dumps(data),
        )

    jsondata = json.loads(r.text)
    response = json.dumps({'satoshis': satamount, 'lnurl': jsondata['lnurl']})

    #p.qr(jsondata['lnurl'],ec=0,size=10)
    #p.cut()

    #return jsondata['lnurl'] #"QR Code printed"
    return response

app.run(host='0.0.0.0',port=5000)
