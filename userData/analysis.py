import json
import statistics
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import MaxNLocator

meanpointprops = dict(marker='D', markeredgecolor='black',
                  markerfacecolor='firebrick')

with open('renewedSubUserData.json') as jsonData:
  data = json.load(jsonData)

"""

This data plots user data with their associated scan statistics.

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

def portal_login_plot():

    portalLoginStatisticsDict = {}

    portalLoginList = []

    for userID in data:
        # key = userID
        userDict = data[userID]
        portalLogin = userDict.get('Portal Login')
        portalLoginList.append(portalLogin)

    meanPortalLogin = round(statistics.mean(portalLoginList))
    medianPortalLogin = round(statistics.median(portalLoginList))
    modePortalLogin = round(statistics.mode(portalLoginList))
    sumPortalLogin = sum(portalLoginList)
    TotalUsers = len(portalLoginList)



    plt.hist(portalLoginList,density=0, bins=range(0,20), edgecolor='black')


    plt.xlim(0, 20)

    plt.title('Portal Logins in 10-day trial', fontsize=14, ha='center')
    plt.xlabel("# of Portal Logins")
    plt.ylabel("Count")
    plt.figtext(.25,.8,"Mean = " + str(meanPortalLogin)+" Logins",fontsize=10, ha='left')
    plt.figtext(.25,.75,"Median = " + str(medianPortalLogin)+ " Logins",fontsize=10, ha='left')
    plt.figtext(.25,.7,"Mode = " + str(modePortalLogin)+ " Logins",fontsize=10, ha='left')
    plt.figtext(.75,.8,"Total = " + str(sumPortalLogin)+ " Logins",fontsize=10, ha='right')
    plt.figtext(.75,.75,"N = " + str(TotalUsers)+ " Users",fontsize=10, ha='right')

    plt.locator_params(axis='x', integer=True)

    plt.show()


    fig2, ax1 = plt.subplots()
    ax1.set_title('Box Plot of Portal Logins')
    ax1.boxplot(portalLoginList,showfliers=False,vert=False,meanline=True,showbox=True,manage_ticks=True)

    quantiles = np.quantile(portalLoginList, np.array([0.25, 0.50, 0.75]))
    ax1.vlines(quantiles, [0] * quantiles.size, [1] * quantiles.size, color='b', ls=':', lw=0.5, zorder=0)
    ax1.set_ylim(0.5, 1.5)
    ax1.set_xticks(quantiles)

    plt.xlabel("Count of Portal Logins")
    plt.ylabel("")
    plt.show()


def scan_saved_plot():

    scanSavedStatisticsDict = {}

    scanSavedList = []

    for userID in data:
        # key = userID
        userDict = data[userID]
        scanSaved = userDict.get('Scan Saved')
        scanSavedList.append(scanSaved)

    meanScanSaved = round(statistics.mean(scanSavedList))
    medianScanSaved = round(statistics.median(scanSavedList))
    modeScanSaved = round(statistics.mode(scanSavedList))

    sumScanSaved = sum(scanSavedList)
    TotalUsers = len(scanSavedList)

    plt.hist(scanSavedList,density=0, bins=range(0,30), edgecolor='black')

    plt.xlim(0, 30)

    plt.title('Scans Saved in 10-day trial', fontsize=14, ha='center')
    plt.suptitle("n = 120", y=1.05, fontsize=18)
    plt.xlabel("# of Scans Saved")
    plt.ylabel("Count")
    plt.figtext(.25,.8,"Mean = " + str(meanScanSaved)+" scans",fontsize=10, ha='left')
    plt.figtext(.25,.75,"Median = " + str(medianScanSaved)+ " scans",fontsize=10, ha='left')
    plt.figtext(.25,.7,"Mode = " + str(modeScanSaved)+ " scans",fontsize=10, ha='left')
    plt.figtext(.75,.8,"Total = " + str(sumScanSaved)+ " scans",fontsize=10, ha='right')
    plt.figtext(.75,.75,"N = " + str(TotalUsers)+ " Users",fontsize=10, ha='right')

    plt.show()

    fig2, ax1 = plt.subplots()
    ax1.set_title('Box Plot of Scans Saved')
    ax1.boxplot(scanSavedList,showfliers=False,vert=False,meanline=True)
    plt.xlabel("# of Scans Saved")
    plt.ylabel("")
    plt.show()


    fig2, ax1 = plt.subplots()
    ax1.set_title('Box Plot of Scans Saved')
    ax1.boxplot(scanSavedList,showfliers=False,vert=False,showbox=True,manage_ticks=True,meanprops=meanpointprops,
                   showmeans=True)

    quantiles = np.quantile(scanSavedList, np.array([0.25, 0.50, 0.75]))
    ax1.vlines(quantiles, [0] * quantiles.size, [1] * quantiles.size, color='b', ls=':', lw=0.5, zorder=0)
    ax1.set_ylim(0.5, 1.5)
    ax1.set_xticks(quantiles)

    plt.xlabel("# of Scans Saved")
    plt.ylabel("")
    plt.show()





def scan_started_plot():

    scanStartedStatisticsDict = {}

    scanStartedList = []

    for userID in data:
        # key = userID
        userDict = data[userID]
        scanStarted = userDict.get('Scan Started')
        scanStartedList.append(scanStarted)

    meanScanStarted = round(statistics.mean(scanStartedList))
    medianScanStarted = round(statistics.median(scanStartedList))
    modeScanStarted = round(statistics.mode(scanStartedList))
    TotalUsers = len(scanStartedList)

    sumScanStarted = sum(scanStartedList)

    plt.hist(scanStartedList,density=0, bins=range(0,60), edgecolor='black')

    plt.xlim(0, 60)

    plt.title('Distribution of Scans Started in 10-day trial', fontsize=14, ha='center')
    plt.xlabel("# of Scans Started")
    plt.ylabel("Count")
    plt.figtext(.25,.8,"Mean = " + str(meanScanStarted)+" scans",fontsize=10, ha='left')
    plt.figtext(.25,.75,"Median = " + str(medianScanStarted)+ " scans",fontsize=10, ha='left')
    plt.figtext(.25,.7,"Mode = " + str(modeScanStarted)+ " scans",fontsize=10, ha='left')
    plt.figtext(.75,.8,"Total = " + str(sumScanStarted)+ " scans",fontsize=10, ha='right')
    plt.figtext(.75,.75,"N = " + str(TotalUsers)+ " Users",fontsize=10, ha='right')

    plt.locator_params(axis='x', integer=True)


    plt.show()

    fig2, ax1 = plt.subplots()
    ax1.set_title('Box Plot of Scans Started ')
    ax1.boxplot(scanStartedList,showfliers=False,vert=False,meanline=True)
    plt.xlabel("Count of Scans Started")
    plt.ylabel("")
    plt.show()

    fig2, ax1 = plt.subplots()
    ax1.set_title('Box Plot of Scans Started')
    ax1.boxplot(scanStartedList,showfliers=False,vert=False,showbox=True,manage_ticks=True,meanprops=meanpointprops,
                   showmeans=True)

    quantiles = np.quantile(scanStartedList, np.array([0.25, 0.50, 0.75]))
    ax1.vlines(quantiles, [0] * quantiles.size, [1] * quantiles.size, color='b', ls=':', lw=0.5, zorder=0)
    ax1.set_ylim(0.5, 1.5)
    ax1.set_xticks(quantiles)

    plt.xlabel("# of Scans Started")
    plt.ylabel("")
    plt.show()



def portal_download_plot():

    portalDownloadStatisticsDict = {}

    portalDownloadList = []

    for userID in data:
        # key = userID
        userDict = data[userID]
        portalDownload = userDict.get('Portal Download')
        portalDownloadList.append(portalDownload)

    meanPortalDownload = round(statistics.mean(portalDownloadList))
    medianPortalDownload = round(statistics.median(portalDownloadList))
    modePortalDownload = round(statistics.mode(portalDownloadList))
    sumPortalDownload = sum(portalDownloadList)
    TotalUsers = len(portalDownloadList)

    plt.hist(portalDownloadList, density=0, bins=range(0,20),  edgecolor='black')
    plt.title('Files Downloaded in 10-day trial', fontsize=14, ha='center')
    plt.xlabel("# of Files Downloaded")
    plt.ylabel("Count")
    plt.xlim(0, 20)

    plt.figtext(.25,.8,"Mean = " + str(meanPortalDownload)+" Downloads",fontsize=10, ha='left')
    plt.figtext(.25,.75,"Median = " + str(medianPortalDownload)+ " Downloads",fontsize=10, ha='left')
    plt.figtext(.25,.7,"Mode = " + str(modePortalDownload)+ " Downloads",fontsize=10, ha='left')
    plt.figtext(.75,.8,"Total = " + str(sumPortalDownload)+ " Downloads",fontsize=10, ha='right')
    plt.figtext(.75,.75,"N = " + str(TotalUsers)+ " Users",fontsize=10, ha='right')

    plt.locator_params(axis='x', integer=True)

    plt.show()

    fig2, ax1 = plt.subplots()
    ax1.set_title('Box Plot of Scans Downloaded ')
    ax1.boxplot(portalDownloadList,showfliers=False,vert=False,meanline=True)
    plt.xlabel("Count of Scans Downloaded")
    plt.ylabel("")
    plt.show()

    fig2, ax1 = plt.subplots()
    ax1.set_title('Box Plot of Scans Downloaded')
    ax1.boxplot(portalDownloadList,showfliers=False,vert=False,showbox=True,manage_ticks=True,meanprops=meanpointprops,
                   showmeans=True)

    quantiles = np.quantile(portalDownloadList, np.array([0.25, 0.50, 0.75]))
    ax1.vlines(quantiles, [0] * quantiles.size, [1] * quantiles.size, color='b', ls=':', lw=0.5, zorder=0)
    ax1.set_ylim(0.5, 1.5)
    ax1.set_xticks(quantiles)

    plt.xlabel("# of Scans Downloaded")
    plt.ylabel("")
    plt.show()


def scan_duration_plot():

    scanDurationtatisticsDict = {}

    scanDurationList = []

    for userID in data:
        # key = userID
        userDict = data[userID]
        userScanDurationList = userDict.get('Scan Duration')
        for i in userScanDurationList:

            scanDurationList.append(i)

    meanScanDurationList = round(statistics.mean(scanDurationList))
    medianScanDurationList = round(statistics.median(scanDurationList))
    modeScanDurationList = round(statistics.mode(scanDurationList))

    countScans = round(len(scanDurationList))

    plt.hist(scanDurationList, density=0, bins=range(200),  edgecolor='black')
    plt.title('Distribution of Scan Durations', fontsize=14, ha='center')
    plt.xlabel("Duration of Scan (sec)")
    plt.ylabel("Frequency")

    plt.figtext(.25,.8,"Mean = " + str(meanScanDurationList)+" Seconds",fontsize=10, ha='left')
    plt.figtext(.25,.75,"Median = " + str(medianScanDurationList)+ " Seconds",fontsize=10, ha='left')
    plt.figtext(.25,.7,"Mode = " + str(modeScanDurationList)+ " Seconds",fontsize=10, ha='left')
    plt.figtext(.8,.8,"Sample Size = " + str(countScans)+ " Scans",fontsize=10, ha='right')
    plt.figtext(.75,.75,"N = 117 Users",fontsize=10, ha='right')
    
    plt.locator_params(axis='x', integer=True)
    plt.show()


    fig2, ax1 = plt.subplots()
    ax1.set_title('Box Plot of Scan Durations')
    ax1.boxplot(scanDurationList,showfliers=False,vert=False,meanline=True)
    plt.xlabel("Duration of Scan (sec)")
    plt.ylabel("")
    plt.show()

    fig2, ax1 = plt.subplots()
    ax1.set_title('Box Plot of Scan Durations')
    ax1.boxplot(scanDurationList,showfliers=False,vert=False,meanline=True,showbox=True,manage_ticks=True)

    quantiles = np.quantile(scanDurationList, np.array([0.25, 0.50, 0.75]))
    ax1.vlines(quantiles, [0] * quantiles.size, [1] * quantiles.size, color='b', ls=':', lw=0.5, zorder=0)
    ax1.set_ylim(0.5, 1.5)
    ax1.set_xticks(quantiles)

    plt.xlabel("Count of Scan Durations")
    plt.ylabel("")
    plt.show()


def scan_duration_plot_none():
    # analyzing scan duration data but excluding durations < 5

    scanDurationtatisticsDict = {}

    scanDurationList = []

    for userID in data:
        # key = userID
        userDict = data[userID]
        userScanDurationList = userDict.get('Scan Duration')
        for i in userScanDurationList:
            if i < 5:
                pass
            else:
                scanDurationList.append(i)

    meanScanDurationList = round(statistics.mean(scanDurationList))
    medianScanDurationList = round(statistics.median(scanDurationList))
    modeScanDurationList = round(statistics.mode(scanDurationList))

    plt.hist(scanDurationList, density=0, bins=range(200),  edgecolor='black')
    plt.title('Scan Duration in 10-day trial (sec > 5)', fontsize=14, ha='center')
    plt.xlabel("Duration of Scan (sec)")
    plt.ylabel("Count")

    plt.figtext(.25,.8,"Mean = " + str(meanScanDurationList)+" seconds",fontsize=10, ha='left')
    plt.figtext(.75,.8,"Median = " + str(medianScanDurationList)+ " seconds",fontsize=10, ha='right')
    plt.figtext(.5,.75,"Mode = " + str(modeScanDurationList)+ " seconds",fontsize=8, ha='center')


    plt.locator_params(axis='x', integer=True)

    plt.show()


def main():
     portal_login_plot()
     scan_saved_plot()
     scan_started_plot()
     portal_download_plot()
     scan_duration_plot()

if __name__ == "__main__":
    main()
