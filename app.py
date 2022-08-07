from email import parser
from os import getuid
from urllib import request
from pymisp import PyMISP
from pymisp import ExpandedPyMISP
import argparse

#from keys import misp_url, misp_key
import argparse
from flask import Flask , render_template


# # For python2 & 3 compat, a bit dirty, but it seems to be the least bad one
# try:
#     input = raw_input
# except NameError:
#     pass

# def init(url, key):
#     return PyMISP(url, key, True, 'json', debug=True)
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
app=Flask(__name__)
misp = ExpandedPyMISP('https://192.168.1.12', 'Py7YJe1sBr1LcsHIroFmpdektP1eYPbWUI2miW4T',ssl=False,debug=False,proxies=None,cert=None,auth=None,tool='',timeout=None)

@app.route("/",methods=['GET'])

def create_app():
    #print (PyMISP.get_attribute[0])
    #req =PyMISP(url="https://192.168.1.12/galaxies",key="Py7YJe1sBr1LcsHIroFmpdektP1eYPbWUI2miW4T",ssl=False,debug=False,proxies=None,cert=None,auth=None,tool='',timeout=None)
   # req = request.get('https://192.168.1.12/galaxies')
   #  #  print (req.get_event.__str__)
    parser = argparse.ArgumentParser(description='Get an event from a MISP instance.')
    # parser.add_argument("-e", "--event", required=True, help="Event ID to get.")
    # parser.add_argument("-o", "--output", help="Output file")

    #args = parser.parse_args()
    print (parser)

    print ("hello before")
    args, _ = parser.parse_known_args()
    print(args)

    print ("hello after")

    misp = ExpandedPyMISP('https://192.168.1.12', 'Py7YJe1sBr1LcsHIroFmpdektP1eYPbWUI2miW4T',ssl=False,debug=False,proxies=None,cert=None,auth=None,tool='',timeout=None)
    print (misp.galaxies())

    # event = misp.get_event(args.event, pythonify=True)
    # if args.output:
    #     with open(args.encodings.output, 'w') as f:
    #         f.write(event.to_json())
    # else:
    #     print(event.to_json())

    return ("hello")

@app.route("/events",methods=['GET'])

def getEvents():
        
  return(misp.events())

@app.route("/attribute",methods=['GET'])

def getAttributes():
        
  return(misp.attributes())
@app.route("/add",methods=['GET'])

def addE():
        
  return(misp.add_event())