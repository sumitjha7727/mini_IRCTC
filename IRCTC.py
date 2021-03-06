import requests

'''
This Project is done On Some Of The Features Of IRCTC Application.
Railway API is used.

Created On: 31-03-2021 using PyCharm Comunity Edition 2019.3.4
Created By: Sumit Kant Jha
'''


def user_menu():
    user_input = input("""
    Hi. How can we help you ? Press...
    1. To find train route
    2. To check PNR status
    3. To check seat availability
    4. To find train running status
    5. To exit
    """)

    if user_input == "1":
        print("Find train route")
        print("---------------------------------")
        train_route()
    elif user_input == "2":
        print("Find PNR status")
        print("---------------------------------")
        pnr_status()
    elif user_input == "3":
        print("Check seat availability")
        print("---------------------------------")
        availability()
    elif user_input == "4":
        print("Train Status")
        print("---------------------------------")
        live_status()
    else:
        print("BYE")


def train_route():
    train = input("Enter the train number: ")
    print("---------------------------------")
    url = "https://api.railwayapi.com/v2/route/train/{}/apikey/ho9oyhc362/".format(train)
    response = requests.get(url)
    response = response.json()
    # print(response)
    for i in response['route']:
        print(i['station']['name'], "|", i['scharr'], "|", i['schdep'])


def pnr_status():
    pnr = input("Enter the PNR number: ")
    print("---------------------------------")
    url = "https://api.railwayapi.com/v2/pnr-status/pnr/{}/apikey/ho9oyhc362/".format(pnr)
    response = requests.get(url)
    response = response.json()
    # print(response)
    print("current status:", (response.get("passengers"))[0].get('current_status'))
    print("---------------------------------")
    print("Train Details:", (response.get("train")).get("name"), "|", (response.get("train")).get("number"))
    print("---------------------------------")
    print("From:", (response.get("from_station")).get("name"), "To:", (response.get("reservation_upto")).get("name"),
          "On:", response.get("doj"))


def availability():
    train = input("Enter the train number:")
    print("---------------------------------")
    stn_code = input("Enter the source station code:")
    print("---------------------------------")
    des_code = input("Enter the destination station code:")
    print("---------------------------------")
    date = input("Enter the date in dd-mm-yyy format:")
    print("---------------------------------")
    prefer = input("Enter the class i.e 1A,2A,3A,CC,SL: ")
    print("---------------------------------")
    quota = input("Enter the quota i.e General~GN by default: ")
    print("---------------------------------")
    url = "https://api.railwayapi.com/v2/check-seat/train/{}/source/{}/dest/{}/date/{}/pref/{}/quota/{}/apikey/ho9oyhc362/".format(
        train, stn_code, des_code, date, prefer, quota)
    response = requests.get(url)
    response = response.json()
    # print(response)
    print("Seat Availability on {}".format(date), "in train no:{}".format(train), "is: ",
          (response.get("availability")[0]).get("status"))
    print("---------------------------------")


def live_status():
    train = input("Enter the train number:")
    print("---------------------------------")
    stn_code = input("Enter the station code to get the status:")
    print("---------------------------------")
    date = input("Enter the date in dd-mm-yyy format:")
    print("---------------------------------")
    url = "https://api.railwayapi.com/v2/live/train/{}/station/{}/date/{}/apikey/ho9oyhc362/".format(train, stn_code,
                                                                                                     date)
    response = requests.get(url)
    response = response.json()
    # print(response)
    # print(response.get("start_date"))
    print("Schedule_Arrival_Date | Actual_Arrival_Date :", (response.get("status")).get("scharr_date"), "|",
          (response.get("status")).get("actarr_date"))
    print("---------------------------------")
    print(response.get("position"))
    print("---------------------------------")
    print("Schedule_Arrival | Schedule_Departure :", (response.get("status")).get("scharr"), "|",
          (response.get("status")).get("schdep"))
    print("---------------------------------")
    print("Actual_Arrival | Actual_Departure :", (response.get("status")).get("actarr"), "|",
          (response.get("status")).get("actdep"))
    print("---------------------------------")
    print("Late In Minutes: ", (response.get("status")).get("latemin"))
    print("---------------------------------")


user_menu()
Hi.How can we help you ? Press...
1. To find train route
2. To check PNR status
3. To check seat availability
4. To find train running status
5. To exit
4
Train Status
---------------------------------
Enter the train number: 13132
---------------------------------
Enter the station code to get the status: DRG
---------------------------------
Enter the date in dd - mm - yyyy format: 24 - 06 - 2019
---------------------------------
Schedule_Arrival_Date | Actual_Arrival_Date: None | None
---------------------------------
None
---------------------------------
Schedule_Arrival | Schedule_Departure: None | None
---------------------------------
Actual_Arrival | Actual_Departure: None | None
---------------------------------
Late In Minutes: None
---------------------------------
