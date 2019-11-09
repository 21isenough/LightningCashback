#!/usr/bin/python

import lightningqr, json

jsondata = json.loads(lightningqr.generate_lnurl(0.01))

print(jsondata['satoshis'],jsondata['lnurl'])
