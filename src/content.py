import json
import codecs
from datetime import date
from flask import Blueprint, request

content_api = Blueprint('content_api', __name__)

#@content_api.route("/getcontent/<int:year>/<int:month>/<int:day>")
#def getTrafficData(year, month, day):
@content_api.route("/getcontent")
def getcontent():
   obj = {
      "id": 1,
      "Speed": 13.04,
       "TravelTime": 408,
       "Status": 0,
       "DataAsOf": "10/23/2017 15:10:15",
       "linkId": 4616337,
       "linkPoints": "40.74047,-74.009251 40.74137,-74.00893 40.7431706,-74.008591 40.7462304,-74.00797 40.74812,-74.007651 40.748701,-74.007691 40.74971,-74.00819 40.75048,-74.008321 40.751611,-74.00789 40.7537504,-74.00704 40.75721,-74.00463 40.76003,-74.002631 40.7607405,-7",
       "EncodedPolyLine": "}btwFx|ubMsD_AgJcAcR{ByJ_AsBFiEbByCXaFuAkLiDsTaNsPoKmCmB",
       "EncodedPolyLineLvls": "BBBBBBBBBBBBB",
       "Owner": "NYC_DOT_LIC",
       "Transcom_id": 4616337,
       "Borough": "Manhattan",
       "linkName": "11th ave n ganservoort - 12th ave @ 40th st"
      }

   try:
      f = open('../datasource/10_23_2017_22_08.json', 'r')
   except IOError:
      return json.dumps({'message': 'no information for given date'}), 500

   #return json.dumps(obj), 200
   return json.dumps(json.load(f)), 200
