#!/usr/bin/python3

import mysql.connector
import json

'''
{
    'items': [
        ['name':'coffee', 'qty':'2', 'unit_price':'1', 'total_price':'1']
    ]

    'ammounts': [
        ['']
    ]
}

'''



#get info from the database

#placeholders for the variables
orderdict = {
    'items': [
        {'name':'coffee', 'qty':2, 'unit_price':1.5, 'total_price': 3},
        {'name':'coffee', 'qty':1, 'unit_price':1.5, 'total_price': 1.5}
    ],

    'ammounts': {
        'total' : 3.5,
        'payed' : 5,
        'change':{
            'eur':1.5,
            'satishi':1234
        }
    }
}


#generate lightning request

#compile everything on a json

orderjson = json.dumps(orderdict)


