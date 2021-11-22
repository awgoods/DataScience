"""
This script assocates a scan's duration with it's type.

This dictionary assigns a list of durations to their scanType
    scanTypeDictionary = {
    'TLSO':[],
    'Arm':[],
    'BK':[],
    'KAFO':[],
    'AFO':[],
    'FO':[],
    'TLSO Small':[],
    'KO':[],
    }

    This dictionary calculates statistics from that duration lists

    scanTypeStatsDictionary = {
    # [Mean, Median, mode, standard dev, count]
    'TLSO':[],
    'Arm':[],
    'BK':[],
    'KAFO':[],
    'AFO':[],
    'FO':[],
    'TLSO Small':[],
    'KO':[],
    }


"""

import json
import statistics
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


with open('data.json') as jsonData:
  data = json.load(jsonData)

"""
Data structure of 'data'
{'user0':
    {
        'Scan Type': ['Arm', 'BK'],
        'Scan Started': 2,
        'Scan Duration': [31, 5],
        'Scan Completed': 2,
        'Scan Saved': 0,
        'Portal Download': 0,
        'Portal Login': 1

    } ,
'user1':
    {
        'Scan Type': ['TLSO', 'TLSO', 'TLSO', 'TLSO', 'TLSO', 'TLSO', 'TLSO', 'TLSO', 'TLSO', 'TLSO', 'TLSO', 'TLSO', 'TLSO', 'TLSO', 'TLSO', 'TLSO', 'TLSO', 'TLSO', 'TLSO', 'TLSO', 'TLSO', 'TLSO', 'TLSO', 'TLSO', 'TLSO', 'TLSO', 'TLSO', 'TLSO', 'TLSO', 'TLSO', 'TLSO', 'TLSO'],
        'Scan Started': 32,
        'Scan Duration': [50, 26, 16, 19, 7, 26, 5, 11, 8, 7, 8, 7, 5, 10, 10, 8, 8, 11, 7, 10, 25, 2, 34, 29, 31, 7, 20, 6, 11, 6, 4, 12],
        'Scan Completed': 32,
        'Scan Saved': 4,
        'Portal Download': 13,
        'Portal Login': 2
    },
    ...
}
"""
def scan_type():

    # Total scans completed by type: {'TLSO': 153, 'Arm': 526, 'BK': 431, 'KAFO': 35, 'AFO': 347, 'FO': 104, 'TLSO Small': 26, 'KO': 75}

    scanTypeUserList = {
    #Each index in the list represents a total count of scanType Started by each user. The length of the list is equal to the population size.
    # ex. TLSO: [3, 4 ,0] Means User#1 scanned a tlso 3 times, user#2 scanned a tlso 4 times, and user#3 scanned tlso 0 times
    'TLSO':[],
    'Arm':[],
    'BK':[],
    'KAFO':[],
    'AFO':[],
    'FO':[],
    'TLSO Small':[],
    'KO':[],
    }


    for userID in data:
        # key = userID
        userDict = data[userID]
        userScanTypeList = userDict['Scan Type']

        userScanTypeCount = {
        'TLSO':0,
        'Arm':0,
        'BK':0,
        'KAFO':0,
        'AFO':0,
        'FO':0,
        'TLSO Small':0,
        'KO':0,
        }

        for i in userScanTypeList:
            # adds 1 to the user dictionary to count which scans they've completed
            userScanTypeCount[i] += 1

        for key in userScanTypeCount:

            userCount = userScanTypeCount[key]

            scanTypeUserList[key].append(userCount)


    # now I will calcuate statistics from the scan type count dictionary
    scanTypeCountStatsDictionary = {
    # [Mean, Median, mode, standard dev, number of scans]
    'TLSO':[],
    'Arm':[],
    'BK':[],
    'KAFO':[],
    'AFO':[],
    'FO':[],
    'TLSO Small':[],
    'KO':[],
    }

    for i in scanTypeUserList:

        scanTypeCountList = scanTypeUserList[i]

        meanCount = round(statistics.mean(scanTypeCountList))
        medianCount = round(statistics.median(scanTypeCountList))
        modeCount = round(statistics.mode(scanTypeCountList))
        stDevCount = round(statistics.stdev(scanTypeCountList))
        numberOfScans = sum(scanTypeCountList)

        scanTypeCountStatsDictionary[i].append(meanCount)
        scanTypeCountStatsDictionary[i].append(medianCount)
        scanTypeCountStatsDictionary[i].append(modeCount)
        scanTypeCountStatsDictionary[i].append(stDevCount)
        scanTypeCountStatsDictionary[i].append(numberOfScans)


    # Code to create plot of statistics

    scanTypeCountMeanDictionary = {}
    scanTypeCountStDevDictionary = {}
    negativeError = []
    # [Mean, Median, mode, standard dev, count]

    for i in scanTypeCountStatsDictionary:
        Stats = scanTypeCountStatsDictionary[i]
        scanTypeCountMeanDictionary[i] = Stats[0]

    for i in scanTypeCountStatsDictionary:
        Stats = scanTypeCountStatsDictionary[i]
        scanTypeCountStDevDictionary[i] = Stats[3]
        negativeError.append(0)

    keys = scanTypeCountMeanDictionary.keys()
    values = scanTypeCountMeanDictionary.values()
    error = scanTypeCountStDevDictionary.values()


    fig1, ax1 = plt.subplots()
    ax1.bar(keys, values,yerr= (negativeError,error), color='blue', edgecolor='black',align='center', capsize=4)
    ax1.set_ylabel('Average Count')
    ax1.set_xlabel('Scan Type')
    ax1.set_title('Average Profile of Scans started during trial (by Type)')
    plt.show()

    # Pie chart of average profile:

    fig2, ax2 = plt.subplots()
    ax2.pie(values, labels=keys)
    ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()
    print(scanTypeCountStatsDictionary)

def duration_type():

    scanTypeDictionary = {
    'TLSO':[],
    'Arm':[],
    'BK':[],
    'KAFO':[],
    'AFO':[],
    'FO':[],
    'TLSO Small':[],
    'KO':[],
    }

    errors = 0

    for userID in data:
    #use for loop to move through data structure

        userDict = data[userID]
        # store each user's data as a dictionary

        #Grab the lists we need from the user dictionary
        scanTypeList = userDict['Scan Type']
        scanDurationList = userDict['Scan Duration']

        #scanTypeList example = ['AFO', 'AFO', 'AFO']
        #scanDurationList example = [72, 12, 38]


        index = 0

        while index < len(scanTypeList):
            # loop through the scan-type list. This while loop will try to pair each scan-type with an associated duration.
            #using try/except to catch corrupt data. Sometimes a scanType does not have a paired duration value. Maybe App crashed mid-scan?

            try:
                scanDuration = scanDurationList[index]
                scanType = scanTypeList[index]
                scanTypeDictionary[scanType].append(scanDuration)
                #for each loop through a users' list, append the master dictionary to track duration of scans / scantype relationship
                #We can do this assuming the index of the duration / type list are 1:1 related. Likely the case becuase lists are immutable and order is cemented.

            except IndexError:
                pass

            index += 1
    return scanTypeDictionary


def duration_type_plot():

    #this function plots data taken from the scanDuration list

    typeDurationDict = duration_type()


    scanTypeStatsDictionary = {
    # [Mean, Median, mode, standard dev, count]
    'TLSO':[],
    'Arm':[],
    'BK':[],
    'KAFO':[],
    'AFO':[],
    'FO':[],
    'TLSO Small':[],
    'KO':[],
    }

    for i in typeDurationDict:
        scanTypeList = typeDurationDict[i]

        meanDuration = round(statistics.mean(scanTypeList))
        medianDuration = round(statistics.median(scanTypeList))
        modeDuration = round(statistics.mode(scanTypeList))
        stDevDuration = round(statistics.stdev(scanTypeList))
        numberOfScans = round(len(scanTypeList))
        scanTypeStatsDictionary[i].append(meanDuration)
        scanTypeStatsDictionary[i].append(medianDuration)
        scanTypeStatsDictionary[i].append(modeDuration)
        scanTypeStatsDictionary[i].append(stDevDuration)
        scanTypeStatsDictionary[i].append(numberOfScans)


    fig, ax = plt.subplots()
    bp = ax.boxplot(typeDurationDict.values(),meanline=True,sym='+',whis=1.5)
    plt.setp(bp['boxes'], color='black')
    plt.setp(bp['whiskers'], color='black')
    plt.setp(bp['fliers'], color='red', marker='+')
    ax.set_xticklabels(typeDurationDict.keys())
    ax.set_axisbelow(True)
    ax.set_title('Duraction of Scan Type Completed')
    ax.set_xlabel('Scan Type')

    ax.set_ylabel('Scan Duration (sec)')
    plt.show()

    scanTypeMeanDictionary = {}
    scanTypeStDevDictionary = {}
    negativeError = []
    # [Mean, Median, mode, standard dev, count]



    for i in scanTypeStatsDictionary:
        Stats = scanTypeStatsDictionary[i]
        scanTypeMeanDictionary[i] = Stats[0]

    for i in scanTypeStatsDictionary:
        Stats = scanTypeStatsDictionary[i]
        scanTypeStDevDictionary[i] = Stats[3]
        negativeError.append(0)

    keys = scanTypeMeanDictionary.keys()
    values = scanTypeMeanDictionary.values()
    error = scanTypeStDevDictionary.values()


    fig1, ax1 = plt.subplots()
    ax1.bar(keys, values,yerr= (negativeError,error), color='blue', edgecolor='black',align='center', capsize=4)
    ax1.set_ylabel('Scan Duration (sec)')
    ax.set_xlabel('Scan Type')
    ax1.set_title('Mean Duration of Scans by Type')
    plt.show()


# Do it again but take out scans that are 0, 1, or 2 seconds.
# Make sure proper user list is being used??? Confirm data source
# For the scans that are saved, what was their duration???? This would create a bad-scan or good-scan threshould based on historical data

def main():
    scan_type()
if __name__ == "__main__":
    main()
