"""
This script pulls user data from a given list in Klayvio. For each user in that list, specific metrics are pulled from their timeline. Each user is stored in a dictionary with their aggregate lifetime metrics"
"""
import requests
import json
# Private API key


payload = {'api_key': 'pk_ee24d57ec5ff42346ae78f25338c0bea1f'}
metricID = {'QYfxya'}



def deviceID(userID):
    # Portal Login Metric ID = 'QYfxya'

    https = 'https://a.klaviyo.com/api/v1/person/' + userID + '/metric/QYfxya/timeline'
    deviceIDRequest = requests.get(https,params=payload)
    deviceIDResponse = deviceIDRequest.json()
    deviceIDCount = deviceIDResponse["count"]


    #userSecurityList = [List of Unique Initiral Device IDs]
    userSecurityList = []
    count = 0
    while count < deviceIDCount:
    # Code to parse through json response and find data
        deviceIDData = deviceIDResponse["data"]
        DeviceIDEventPropertiesDict = deviceIDData[count]
        uniqueIDDict = DeviceIDEventPropertiesDict["event_properties"]
        uniqueDeviceID = uniqueIDDict["Unique Initial Registrations"]

        # append to scan type list for a given user
        userSecurityList.append(uniqueDeviceID)
        count += 1

    # returns number of time a user has registered a device


    return userSecurityList

def getIDList(ListID):

    # List ID = 'WfPEde': Initial Device ID = Yes
    URL = 'https://a.klaviyo.com/api/v2/group/'+ str(ListID) +'/members/all'
    trialSegmentRequest = requests.get(URL , params=payload)

    #use json() method to parse json file
    #Then, get list of users via key specified in Klayvio docs
    response = trialSegmentRequest.json()
    responseList = response['records']

    # Initalize blank list to store user IDs retrieved from trial-started Segment
    idList = []
    for i in responseList:
        idList.append(i['id'])

    # List containing the total number of device
    return idList



def main():
    print('Requesting User Info...')

    #Initialize dictionary to be used for analysis
    securityMeticsDictionary = {}

    """
        # this will be data structure of dictionary

        securityMeticsDictionary = {XXXXXXXXX: [X,Y,Z],

        ...}

    """

    # getIDList returns a list of userIDs from a given segment/list in Klaviyo
    #idList contains list of users to be analyzed
    idList = getIDList('WfPEde')

    # Initialize List of users to be excluded from analysis: Comb/Knockout Employees
    # Segment ID = ScdELN
    exclusionList = getIDList('ScdELN')

    length = len(idList)
    count = 1

    for i in idList:
        if i in exclusionList:
            pass
        else:
            userID = i
            userSecurityList = deviceID(userID)
            index = idList.index(i)

            securityMeticsDictionary[userID] = userSecurityList

        print('Processing Request. Status: ' +str(count) +'/' + str(length))
        count+=1


    print(securityMeticsDictionary)



    with open("securityData.json", "w") as outfile:
        json.dump(securityMeticsDictionary, outfile)



if __name__ == "__main__":
    main()
