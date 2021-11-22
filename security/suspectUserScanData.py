"""
This script pulls user data from a given list in Klayvio. For each user in that list, specific metrics are pulled from their timeline. Each user is stored in a dictionary with their aggregate lifetime metrics"
"""
import requests
import json
# Private API key


payload = {'api_key': 'pk_ee24d57ec5ff42346ae78f25338c0bea1f'}

def scan_type(userID):

    # App Scan Started Metric ID = 'PXvZdM' (contains scan type)

    https = 'https://a.klaviyo.com/api/v1/person/' + userID + '/metric/PXvZdM/timeline'
    AppScanStartedTimelineRequest = requests.get(https,params=payload)
    AppScanStartedTimelineRequest = requests.get(https,params=payload)
    AppScanStartedTimelineResponse = AppScanStartedTimelineRequest.json()
    AppScanStartedCount = AppScanStartedTimelineResponse["count"]


    scanTypeList = []
    count = 0

    while count < AppScanStartedCount:
    # Code to parse through json response and find data
        AppScanStartedTimelineData = AppScanStartedTimelineResponse["data"]
        AppScanStartedTimelineDataEventProperties = AppScanStartedTimelineData[count]
        scanTypeDictionary = AppScanStartedTimelineDataEventProperties["event_properties"]
        scanType = scanTypeDictionary["Scan Type"]

        # append to scan type list for a given user
        scanTypeList.append(scanType)
        count += 1

    # List of scans by type
    # the length of this list is equal to the number of scans started
    return scanTypeList

def scan_duration(userID):
    # App Scan Completed Metric ID = 'LpQJhx' (contains duration)

    https = 'https://a.klaviyo.com/api/v1/person/' + userID + '/metric/LpQJhx/timeline'

    AppScanCompletedTimelineRequest = requests.get(https,params=payload)
    AppScanCompletedTimelineResponse = AppScanCompletedTimelineRequest.json()
    # Number of App Scans Completed, to guide while loop
    AppScanCompletedCount = AppScanCompletedTimelineResponse["count"]

    # Initalize scan duration list
    scanDurationList =[]

    # code to create list of scan durations for a particular user
    count = 0
    while count < AppScanCompletedCount:

    # Code to parse through json response and find data
        AppScanCompletedTimelineData = AppScanCompletedTimelineResponse["data"]
        AppScanCompletedTimelineDataEventProperties = AppScanCompletedTimelineData[count]
        scanDurationDictionary = AppScanCompletedTimelineDataEventProperties["event_properties"]
        scanDuration = scanDurationDictionary["Scan Duration"]

        # append to scan duration list for a given user
        scanDurationList.append(scanDuration)
        count += 1

    # List of durations each scan took (seconds)
    # Length of list is equal to number of scans completed
    return scanDurationList

def scan_saved(userID):
    # App Scan Saved MetricID = 'JaQNVV'

    https = 'https://a.klaviyo.com/api/v1/person/' + userID + '/metric/JaQNVV/timeline'

    AppScanSavedTimelineRequest = requests.get(https,params=payload)
    AppScanSavedTimelineResponse = AppScanSavedTimelineRequest.json()
    AppScanSavedCount = AppScanSavedTimelineResponse["count"]

    # Number of App Scans Saved
    return AppScanSavedCount



def portal_download(userID):
    # Portal Download File Metric ID = 'LvpDef'

    https = 'https://a.klaviyo.com/api/v1/person/' + userID + '/metric/LvpDef/timeline'

    PortalDownloadFileTimelineRequest = requests.get(https,params=payload)
    PortalDownloadFileTimelineResponse = PortalDownloadFileTimelineRequest.json()
    PortalDownloadFileCount = PortalDownloadFileTimelineResponse["count"]

    # Number of files user Downloaded from portal
    return PortalDownloadFileCount




def portal_login(userID):
    # Portal Login Metric ID = 'KbzdNk'

    https = 'https://a.klaviyo.com/api/v1/person/' + userID + '/metric/KbzdNk/timeline'
    PortalLoginTimelineRequest = requests.get(https,params=payload)
    PortalLoginTimelineResponse = PortalLoginTimelineRequest.json()
    PortalLoginTimelineCount = PortalLoginTimelineResponse["count"]

    # returns number of time a user has logged into the portal
    return PortalLoginTimelineCount


def main():
    print('Caluclating Suspect Users Scanning Data')


    idList = ['TsiVsS', '01EMS66GKF10WD9V6V7GAEQCPM', '01EP2XV08SXHYY8M8CA5SRBKWW', '01EN88W5WWS6054SYYQNB90QEF', '01ET3MZNCNFF57WEVKWRR7TJ0G', '01EGT9DY2Q1TEM59C2KRS0BXPG', 'Pc8BmV', 'Ldycx8', '01ES4EA6927Z07D2YEF97JRHTE', '01EG1EX5SKNP2RE2Y69R23YSMB', '01EHYMH4QF0AWBS347PAWRMQG9', 'NRfwJX', '01EP5ED4J89RKK9ZXA91VDYGD9', 'Y9rPUq', '01EVT75H87GC8V4N6B8HYWY2N9', '01EPC36F1C1VYV3FSAA3TJX890', 'VyTdQs', '01EGJJDT2CVVF5GDB1HESE7J01', '01EP73RSS1YEKH45B8ZHC4KJYB', 'H9ZRp5', 'YiqhkZ', '01ET3BN015W41TB94D8Y499PMS', 'XNaTCL', '01EHAHG4KQEDEAEJ7CDKRN4R65', '01EHKN5CTGAQ7X9BKY77DKFAXB', '01EKJ58DE9Y8K77EEHB4WQTRCX', '01EM4QZE5HBM9ZPCRWCS8YD9F4', '01EKJ5M22VFY8DYK141RTCP8NX', '01EK3CHJPACDR4RAXGRDYHTMXP', '01EQ6TG8F9T0T54XTSQP7AMXC9', 'PHMi5r', 'TSDLDm', '01EMM9AKKWDKT0MGRBF3SPV8B0', '01EP53EXA06HE7AQETHK97J6B8', 'Xfn64W']

    PopulationMetricDictionary = {}


    for i in idList:

        # initalize a temporary dictionary to add to master dictionary

        userID = i
        print(i)


        # Collecting data variables
        scanType = scan_type(userID) # List of strings
        scanStarted = len(scanType) # Integer

        scanDuration = scan_duration(userID) # List of integers
        scanCompleted = len(scanDuration) # Integer

        scanSaved = scan_saved(userID) # Integer
        portalDownload = portal_download(userID) # Integer
        portalLogin = portal_login(userID) # Integer


        UserMetricDictionary = {
        "Scan Type": scanType,
        "Scan Started": scanStarted,
        "Scan Duration": scanDuration,
        "Scan Completed": scanCompleted,
        "Scan Saved": scanSaved,
        "Portal Download": portalDownload,
        "Portal Login": portalLogin,
        }

        index = idList.index(i)

        DictKey = "user" + str(index)

        PopulationMetricDictionary[DictKey] = UserMetricDictionary


    print(PopulationMetricDictionary)

    with open("suspectUserScanData.json", "w") as outfile:
        json.dump(PopulationMetricDictionary, outfile)



if __name__ == "__main__":
    main()
