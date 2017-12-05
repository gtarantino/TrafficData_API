import json
import codecs
from datetime import date
from flask import Blueprint, request

content_api = Blueprint('content_api', __name__)

@content_api.route("/getTrafficData")
def getTrafficData():
   try:
      f = open('../datasource/TrafficData.json', 'r')
   except IOError:
      return json.dumps({'message': 'no information for given date'}), 500

   return json.dumps(json.load(f)), 200
