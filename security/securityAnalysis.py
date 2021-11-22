import json
import statistics
import matplotlib.pyplot as plt
import numpy as np
import math

import requests
# Private API key


payload = {'api_key': 'pk_ee24d57ec5ff42346ae78f25338c0bea1f'}


with open('securityData.json') as jsonData:
  data = json.load(jsonData)



def bad_users_profile_builder(badUsersData):

    """
    This function takes in a json object of the form:

    {bad_user_data: [

    {
    USERID: XXXX    => Unique User ID
    AIDR: XXXX      => AIDR = App Initial Device Registrations
    UIR: XXX        => Unique Device Registration
    },

    ]
    }

    And outputs a json object of the form

    {bad_user_dataV2: [

    {
    USERID: XXXX    => Unique User ID
    AIDR: XXXX      => AIDR = App Initial Device Registrations
    UIR: XXX        => Unique Device Registration
    First Name:
    Last Name:
    Organization:
    },

    ]
    }
    Generally, the function appends the bad_user_profile, or "builds" upon it
    """

    badUserList = badUsersData["bad_user_data"]

    # New list of bad_user_data.

    bad_user_dataV2 = {"bad_user_data":[]}

    # This loop through badUserList, takes the ID, retrieves information via Klavyio API, appends new data to bad_user_dataV2
    # bad_user_dataV2 is the finalized dictionary containing bad user information

    for user in badUserList:
        userID = user["ID"]
        https = "https://a.klaviyo.com/api/v1/person/"+str(userID)

        profileRequest = requests.get(https,params=payload)
        profileResponse = profileRequest.json()

        lastName = profileResponse["last_name"]
        firstName = profileResponse["first_name"]
        comapany = profileResponse["Company"]
        email = profileResponse["$email"]


        user["last_name"] = lastName
        user["first_name"] = firstName
        user["Company"] = comapany
        user["email"] = email
        bad_user_dataV2["bad_user_data"].append(user)

    return bad_user_dataV2

def bad_users_structure(badUsers):

    """
    Returns a sctuctred of data of the following form"

    {bad_user_data: [

    {
    USERID: XXXX    => Unique User ID
    AIDR: XXXX      => AIDR = App Initial Device Registrations
    UIR: XXX        => Unique Device Registration
    },

    ]
    }

    """

    badUsersDict = {
    'bad_user_data':[]
    }

    for i in badUsers:

        AIDR = len(badUsers[i])
        UIR = badUsers[i][0]

        securityDict = {
        'ID':i,
        'AIDR': AIDR,
        'UIR':UIR
        }

        badUsersDict['bad_user_data'].append(securityDict)

    return badUsersDict


def no_good_users():
    # returns data set that does not contain good users, only bad users
    #cleans up list of total data. removes good users and keeps bad users.
    bad_users = {} # dictionary of bad users

    for i in data:
        if data[i] == [1]:
            pass
        else:
            bad_users[i] = data[i]
    return bad_users


def good_users_analysis():
    # returns list of user IDs who have not abused secutiy system in-app. App Initial Device ID = [1]

    goodUsers = []

    for i in data:
        if data[i] == [1]:
            goodUsers.append(i)

    AmountOfGoodUsers = len(goodUsers)
    AmountofUsers = len(data)
    goodUsersAnalysis = "Percent of users who have not abused systen: " + str(AmountOfGoodUsers) + " / " + str(AmountofUsers) + " Or " + str(math.trunc(AmountOfGoodUsers/AmountofUsers*100)) + "%"
    print(goodUsersAnalysis)

def main():
    good_users_analysis()
    badUsers = no_good_users()
    badUsersData = bad_users_structure(badUsers)
    badUsersProfile = bad_users_profile_builder(badUsersData)
    print(len(badUsersProfile['bad_user_data']))

    with open("badUsersData.json", "w") as outfile:
        json.dump(badUsersProfile, outfile)

if __name__ == "__main__":
    main()
