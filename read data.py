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

#The class definition below has unnecessary space's before and after object.
class handleInfo( object ):
    
    def write_all(self, file, number_of_items = 10):
        #This file handler 'f' should be closed using f.close() once the operations on the file are done
        f=open(file, 'w')
        data = []
        for i in range(0,number_of_items):
           data+=  [ {"abcedfghijklmnopqrstuvxyz"[random.randint(1,25)] : random.randint(1,100) } ]
        try:
        #Inconsistent use of indentation. 3 spaces instead of 4
        #Dont think try block should be used here
           f.write(json.dumps(data))
        #Inconsistent use of indentation. 3 spaces instead of 4
           logging.debug( "wrote %s lines to the file" % len(data))
        #Dont think except and try block should be used here
        except:
        #Inconsistent use of indentation. 3 spaces instead of 4
           pass

    #This function definition should have self as the first arguement
    def read_all(s, filename):
        #Reads all information from the file and returns a dictionary with the formatted data
        #Unnecessary use of space after f=
        #This file handler 'f' should be closed using f.close() once the operations on the file are done
        f= open(filename)
        #Avoid empty lines like this for code readability
        try:
            yield json.loads( f.readline() )
            logging.info( "Read %s lines of data" % len(json.loads( f.readline() )))
        except:
            pass

a = handleInfo( )
#Unnecessary use of space before "test.txt"
a.write_all(      "test.txt")
#Unnecessary use of space before "next" 
print( next(a.read_all('test.txt')) )

