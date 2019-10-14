#!/usr/bin/python3

import json
import random

from flask import Flask, request, jsonify, render_template, url_for, make_response
import logging

app=Flask(__name__)

@app.route('/api/sunrise', methods=['POST'])
def get_sunrises():
    print(request.json)
    a.write_all("sunrisefile.txt") 
    return('200')

class handleInfo(object):
    
    def write_all(self, file, number_of_items = 10):
                f=open(file, 'w')
        data = []
        for i in range(0,number_of_items):
                   data+=  [{"abcedfghijklmnopqrstuvxyz"[random.randint(1,25)] : random.randint(1,100)}]
        try:
                    f.write(json.dumps(data))
                   logging.debug("wrote %s lines to the file" % len(data))
                except:
                    pass
        f.close()

        def read_all(self, filename):
                f=open(filename)
                try:
                   yield json.loads(f.readline())
                    logging.info("Read %s lines of data" % len(json.loads(f.readline())))
        except:
            pass
        f.close()

a = handleInfo( )
a.write_all("test.txt")
print(next(a.read_all("test.txt")))

