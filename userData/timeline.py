"""
1) This script will find a user's complete metrics timeline
2) Store the timline in a json file
3) Calculate the duration of their saved scans (and which type of scans they were)
4) use this to calcuate a "benchmark time" for what is a good vs. bad scan


This assumes that a user's scan fails mid-scan, and not the end.
This assumes that a user does not save a scan if it's a poor scan


AN Request:

Of people that purchased, were they getting good scans from the beginning (is there a pattern)?
Of the people that purchased, is there any evidence that scanning quality improved over time?
"""

import requests
import json
# Private API key


payload = {'api_key': 'pk_ee24d57ec5ff42346ae78f25338c0bea1f', 'count':150}

userID = 'YqQH25'
https = 'https://a.klaviyo.com/api/v1/person/' + userID + '/metrics/timeline'
jsonResponse = requests.get(https,params=payload)
dictResponse = jsonResponse.json()

ParsedDict = {
}

ParsedDict['Number of Events'] = dictResponse['count']

dataList = dictResponse['data']

i = 0

for metric in dataList:
    print(metric['event_properties'])
    print(metric['event_name'])



"""
[
{
   "event_properties":{
      "Scan File Format":"STL",
      "Scan File Units":"mm",
      "$event_id":"1603221049"
   },
   "uuid":"f6b9c280-1307-11eb-8001-8221f222a8a9",
   "event_name":"App Scan Saved",
   "timestamp":1603221049,
   "object":"event",
   "datetime":"2020-10-20 19:10:49+00:00",
   "person":{
      "updated":"2020-10-20 19:11:07",
      "last_name":"Miller",
      "Cell Phone Type":"iPhone",
      "Mobile Timezone":"America/New_York",
      "$longitude":-85.2406,
      "$email":"carmen.miller@bcm.edu",
      "object":"person",
      "$latitude":34.998,
      "email":"carmen.miller@bcm.edu",
      "$address1":"",
      "$address2":"",
      "$title":"",
      "Company State":"TN",
      "$timezone":"America/New_York",
      "id":"YqQH25",
      "Uses 3d Printing":"no",
      "Customer Description":[
         "Other",
         "Practitioner"
      ],
      "Fabricated in House":"no",
      "$organization":"Pinnacle O&P",
      "$region":"Tennessee",
      "$id":"",
      "first_name":"Carmen",
      "Company":"Pinnacle O&P",
      "created":"2020-07-28 20:25:13",
      "$last_name":"Miller",
      "$phone_number":"5014003494",
      "Uses Central Fabrication":"yes",
      "$country":"United States",
      "$zip":"",
      "Access to iPhone X":"yes",
      "$first_name":"Carmen",
      "$city":"Chattanooga",
      "Company City":"Chattanooga ",
      "Software Used":"N/A"
   },
   "statistic_id":"JaQNVV",
   "id":"3jBQyXFb"
}, ,,,
"""
