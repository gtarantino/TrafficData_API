import json
import codecs
from datetime import date
from flask import Blueprint, request

content_api = Blueprint('content_api', __name__)

#@content_api.route("/getcontent/<int:year>/<int:month>/<int:day>")
#def getTrafficData(year, month, day):
@content_api.route("/getcontent")
def getcontent():
   try:
      f = open('../datasource/10_23_2017_22_08.json', 'r')
   except IOError:
      return json.dumps({'message': 'no information for given date'}), 500

   return json.dumps(json.load(f)), 200

@content_api.route("/getsingletrafficobj")
def getsingletrafficobj():
   try:
      f = open('../datasource/testobj.json', 'r')
   except IOError:
      return json.dumps({'message': 'no information for given date'}), 500

   return json.dumps(json.load(f)), 200
