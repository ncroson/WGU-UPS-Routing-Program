#Nathan Croson
#Student Id: 001192148

import csv
import math
import datetime


# HashTable class using chaining. Code from textbook
class ChainingHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    # O(n)
    def __init__(self, initial_capacity=10):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts a new item into the hash table.
    # O(n)
    def insert(self, key, item):  # does both insert and update
        # get the bucket list where this item will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # update key if it is already in the bucket
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                kv[1] = item
                return True

        # if not, insert the item to the end of the bucket list.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    # O(1)
    def search(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # print(bucket_list)

        # search for the key in the bucket list
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                return kv[1]  # value
        return None

    # Removes an item with matching key from the hash table.
    # O(n)
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])

#creates a class for a Truck object
class Truck:
    def __init__(self, packages, address, mileage, time, truckNumber):
        self.packages = packages
        self.address = address
        self.mileage = mileage
        self.time= time
        self.truckNumber = truckNumber

    def __str__(self):  # overwrite print(Package) otherwise it will print object reference
        return "%s, %s, %s, %s" % (self.packages, self.address, self.mileage, self.time)

#creates a class for a Package object
class Package:
    def __init__(self, package_id, street, city, state, zip, deadline, weight, special_notes):
        self.package_id = package_id
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.special_notes = special_notes
        self.time_delivered = None
        self.delivery_status = False
        self.truckNumber = 0

    def __str__(self):  # overwrite print(Package) otherwise it will print object reference
        return "%s, %s, %s, %s, %s ,%s, %s, %s" % (self.package_id, self.street, self.city, self.state, self.zip, self.deadline, self.weight, self.special_notes)

#Algorithm to find the shortest distance to deliver the packages
#Each package in the truck is looped through
#The second loop compares packages distance and the shortest distance is chosen
#uses Nearest Neighbor algorithm
#uses each indivdual truck as parameter
#O(n^2)
def packageDeliveryAlgoritm(truck):
    print("\nTruck", truck.truckNumber, "Time left hub:", truck.time)

    #loops through every package on the truck
    for i in truck.packages:
        bestPackage = None
        bestDistance = 999999

        #loops through each package id in the truck
        for package_id in truck.packages:
            if truck.time > datetime.timedelta(hours=10, minutes=20):
                p9.street = ("410 S State St")

            #get package information with look up hash table
            package = packageHash.search(package_id)


            #stores the distance between 2 trucks addresss and the package destination
            distance = distance_2d_array[address_dictionary[truck.address]][address_dictionary[package.street]]

            # nearest neighbor algorithm
            #if next package is a shorter distance than previous package checked then it is stored as the best package
            if distance < bestDistance and package.time_delivered == None:
                bestPackage = package
                bestDistance = distance

        #the next package to be delivered is the best package with the shortest distance
        package = bestPackage
        if package != None:

            #records the distance traveled by truck and the time of package deliverey
            distance = distance_2d_array[address_dictionary[truck.address]][address_dictionary[package.street]]
            truck.mileage += distance
            truck.time += datetime.timedelta(minutes=(distance / (18 * (1 / 60))))

            truck.address = package.street
            package.time_delivered = truck.time
            package.delivery_status = True
            package.truckNumber = truck.truckNumber
            print("Package:", package.package_id, "     Truck Number:", truck.truckNumber, "\n  Distance Traveled from previous Address:", distance, "\n  Delivery Time:", package.time_delivered, "  Deadline:", package.deadline, "\n  Address Delivered to: ", package.street, package.city, package.state, package.zip, "\n  Package Weight:", package.weight, "\n  Special Notes:", package.special_notes )
    distance = distance_2d_array[address_dictionary[truck.address]][address_dictionary["4001 South 700 East"]]
    truck.mileage += distance
    truck.time += datetime.timedelta(minutes=(distance / (18 * (1 / 60))))
    print("Truck", truck.truckNumber, "Time arrived at hub:", truck.time, "        Distance to return to hub:", distance)





# create package objects
#O(1)
p1 = Package(1, "195 W Oakland Ave", "Salt Lake City", "UT", 84115, "10:30", 21, "")
p2 = Package(2, "2530 S 500 E", "Salt Lake City", "UT", 84106, "EOD", 44, "")
p3 = Package(3, "233 Canyon Rd", "Salt Lake City", "UT", 84103, "EOD", 2, "Can only be on truck 2")
p4 = Package(4, "380 W 2880 S", "Salt Lake City", "UT", 84115, "EOD", 4, "")
p5 = Package(5, "410 S State St", "Salt Lake City", "UT", 84111,"EOD", 5, "")
p6 = Package(6, "3060 Lester St", "West Valley City", "UT", 84119, "10:30 AM", 88, "Delayed on flight--will not arrive to depot until 9:05 a.m.")
p7 = Package(7, "1330 2100 S", "Salt Lake City", "UT", 84106, "EOD", 8, "")
p8 = Package(8, "300 State St", "Salt Lake City", "UT", 84103, "EOD", 9, "")
p9 = Package(9, "300 State St", "Salt Lake City", "UT", 84103, "EOD", 2, "Wrong address listed")
p10 = Package(10, "600 E 900 South", "Salt Lake City", "UT", 84105,"EOD", 1, "")
p11 = Package(11, "2600 Taylorsville Blvd", "Salt Lake City", "UT", 84118, "EOD", 1, "")
p12 = Package(12, "3575 W Valley Central Station bus Loop", "West Valley City", "UT", 84119, "EOD", 1, "")
p13 = Package(13, "2010 W 500 S", "Salt Lake City", "UT", 84104, "10:30 AM", 2, "")
p14 = Package(14, "4300 S 1300 E", "Millcreek", "UT", 84117, "10:30 AM", 88, "Must be delivered with 15, 19")
p15 = Package(15, "4580 S 2300 E", "Holladay", "UT", 84117, "9:00 AM", 4, "")
p16 = Package(16, "4580 S 2300 E", "Holladay", "UT", 84117, "10:30 AM", 88, "Must be delivered with 13, 19")
p17 = Package(17, "3148 S 1100 W", "Salt Lake City", "UT", 84119, "EOD", 2, "")
p18 = Package(18, "1488 4800 S", "Salt Lake City", "UT", 84123, "EOD", 6, "Can only be on truck 2")
p19 = Package(19, "177 W Price Ave", "Salt Lake City", "UT", 84115, "EOD", 37, "")
p20 = Package(20, "3595 Main St", "Salt Lake City", "UT", 84115, "10:30 AM", 37, "Must be delivered with 13, 15")
p21 = Package(21, "3595 Main St", "Salt Lake City", "UT", 84115, "EOD", 3, "")
p22 = Package(22, "6351 South 900 East", "Murray", "UT", 84121, "EOD", 2, "")
p23 = Package(23, "5100 South 2700 West", "Salt Lake City", "UT", 84118, "EOD", 5, "")
p24 = Package(24, "5025 State St", "Murray", "UT", 84107, "EOD", 7, "")
p25 = Package(25, "5383 S 900 East #104", "Salt Lake City", "UT", 84117, "10:30 AM", 7, "Delayed on flight--will not arrive to depot until 9:05 am")
p26 = Package(26, "5383 S 900 East #104", "Salt Lake City", "UT", 84117, "EOD", 25, "")
p27 = Package(27, "1060 Dalton Ave S", "Salt Lake City", "UT", 84104, "EOD", 5, "")
p28 = Package(28, "2835 Main St", "Salt Lake City", "UT", 84115, "EOD", 7, "Delayed on flight--will not arrive to depot until 9:05")
p29 = Package(29, "1330 2100 S", "Salt Lake City", "UT", 84106, "10:30 AM", 2, "")
p30 = Package(30, "300 State St", "Salt Lake City", "UT", 84103, "10:30 AM", 1, "")
p31 = Package(31, "3365 S 900 W", "Salt Lake City", "UT", 84119, "10:30 AM", 1, "")
p32 = Package(32, "3365 S 900 W", "Salt Lake City", "UT", 84119, "EOD", 1, "Delayed on flight--will not arrive to depot until 9:05 am")
p33 = Package(33, "2530 S 500 E", "Salt Lake City", "UT", 84106, "EOD", 1, "")
p34 = Package(34, "4580 S 2300 E", "Holladay", "UT", 84117, "10:30 AM", 2, "")
p35 = Package(35, "1060 Dalton Ave S", "Salt Lake City", "UT", 84104, "EOD", 88, "")
p36 = Package(36, "2300 Parkway Blvd", "West Valley City", "UT", 84119, "EOD", 88, "Can only be on truck 2")
p37 = Package(37, "410 S State St", "Salt Lake City", "UT", 84111, "10:30 AM", 2, "")
p38 = Package(38, "410 S State St", "Salt Lake City", "UT", 84111, "EOD", 9, "Can only be on truck 2")
p39 = Package(39, "2010 W 500 S", "Salt Lake City", "UT", 84104, "EOD", 9, "")
p40 = Package(40, "380 W 2880 S", "Salt Lake City", "UT", 84115, "10:30 AM", 45, "")


# Hash table instance
#O(1)
packageHash = ChainingHashTable()

# insert package objects into hash table
#O(1)
packageHash.insert(1, p1)
packageHash.insert(2, p2)
packageHash.insert(3, p3)
packageHash.insert(4, p4)
packageHash.insert(5, p5)
packageHash.insert(6, p6)
packageHash.insert(7, p7)
packageHash.insert(8, p8)
packageHash.insert(9, p9)
packageHash.insert(10, p10)
packageHash.insert(11, p11)
packageHash.insert(12, p12)
packageHash.insert(13, p13)
packageHash.insert(14, p14)
packageHash.insert(15, p15)
packageHash.insert(16, p16)
packageHash.insert(17, p17)
packageHash.insert(18, p18)
packageHash.insert(19, p19)
packageHash.insert(20, p20)
packageHash.insert(21, p21)
packageHash.insert(22, p22)
packageHash.insert(23, p23)
packageHash.insert(24, p24)
packageHash.insert(25, p25)
packageHash.insert(26, p26)
packageHash.insert(27, p27)
packageHash.insert(28, p28)
packageHash.insert(29, p29)
packageHash.insert(30, p30)
packageHash.insert(31, p31)
packageHash.insert(32, p32)
packageHash.insert(33, p33)
packageHash.insert(34, p34)
packageHash.insert(35, p35)
packageHash.insert(36, p36)
packageHash.insert(37, p37)
packageHash.insert(38, p38)
packageHash.insert(39, p39)
packageHash.insert(40, p40)

#Table of the distance between address locations
#O(1)
dist_to_WGU = [0,7.2,3.8,11,2.2,3.5,10.9,8.6,7.6,2.8,6.4,3.2,7.6,5.2,4.4,3.7,7.6,2,3.6,6.5,1.9,3.4,2.4,6.4,2.4,5,3.6]#Western Governors University
dist_to_IPG = [7.2,0,7.1,6.4,6,4.8,1.6,2.8,4.8,6.3,7.3,5.3,4.8,3,4.6,4.5,7.4,6,5,4.8,9.5,10.9,8.3,6.9,10,4.4,13] #International Peace Gardens
dist_to_SHP = [3.8,7.1,0,9.2,4.4,2.8,8.6,6.3,5.3,1.6,10.4,3,5.3,6.5,5.6,5.8,5.7,4.1,3.6,4.3,3.3,5,6.1,9.7,6.1,2.8,7.4]#Sugar House Park
dist_to_TBHC = [11,6.4,9.2,0,5.6,6.9,8.6,4,11.1,7.3,1,6.4,11.1,3.9,4.3,4.4,7.2,5.3,6,10.6,5.9,7.4,4.7,0.6,6.4,10.1,10.1]#Taylorsville-Bennion Heritage
dist_to_SLCDHS = [2.2,6,4.4,5.6,0,1.9,7.9,5.1,7.5,2.6,6.5,1.5,7.5,3.2,2.4,2.7,1.4,0.5,1.7,6.5,3.2,5.2,2.5,6,4.2,5.4,5.5]#Salt Lake City Division of Health Services
dist_to_SSLPW = [3.5,4.8,2.8,6.9,1.9,0,6.3,4.3,4.5,1.5,8.7,0.8,4.5,3.9,3,3.8,5.7,1.9,1.1,3.5,4.9,6.9,4.2,9,5.9,3.5,7.2]#South Salt Lake Public Works
dist_to_SLCSS = [10.9,1.6,8.6,8.6,7.9,6.3,0,4,4.2,8,8.6,6.9,4.2,4.2,8,5.8,7.2,7.7,6.6,3.2,11.2,12.7,10,8.2,11.7,5.1,14.2]#Salt Lake City Streets and Sanitation
dist_to_DL = [8.6,2.8,6.3,4,5.1,4.3,4,0,7.7,9.3,4.6,4.8,7.7,1.6,3.3,3.4,3.1,5.1,4.6,6.7,8.1,10.4,7.8,4.2,9.5,6.2,10.7]#Deker Lake
dist_to_SLCOH = [7.6,4.8,5.3,11.1,7.5,4.5,4.2,7.7,0,4.8,11.9,4.7,0.6,7.6,7.8,6.6,7.2,5.9,5.4,1,8.5,10.3,7.8,11.5,9.5,2.8,14.1]#Salt Lake City Ottinger Hall
dist_to_CL = [2.8,6.3,1.6,7.3,2.6,1.5,8,9.3,4.8,0,9.4,1.1,5.1,4.6,3.7,4,6.7,2.3,1.8,4.1,3.8,5.8,4.3,7.8,4.8,3.2,6]#Columbus Library
dist_to_TCH = [6.4,7.3,10.4,1,6.5,8.7,8.6,4.6,11.9,9.4,0,7.3,12,4.9,5.2,5.4,8.1,6.2,6.9,11.5,6.9,8.3,4.1,0.4,4.9,11,6.8]#Taylorsville City Hall
dist_to_SSLP = [3.2,5.3,3,6.4,1.5,0.8,6.9,4.8,4.7,1.1,7.3,0,4.7,3.5,2.6,2.9,6.3,1.2,1,3.7,4.1,6.2,3.4,6.9,5.2,3.7,6.4]#South Salt Lake Police
dist_to_CH = [7.6,4.8,5.3,11.1,7.5,4.5,4.2,7.7,0.6,5.1,12,4.7,0,7.3,7.8,6.6,7.2,5.9,5.4,1,8.5,10.3,7.8,11.5,9.5,2.8,14.1]#Council Hall
dist_to_RP = [5.2,3,6.5,3.9,3.2,3.9,4.2,1.6,7.6,4.6,4.9,3.5,7.3,0,1.3,1.5,4,3.2,3,6.9,6.2,8.2,5.5,4.4,7.2,6.4,10.5]#Redwood Park
dist_to_SLCMH = [4.4,4.6,5.6,4.3,2.4,3,8,3.3,7.8,3.7,5.2,2.6,7.8,1.3,0,0.6,6.4,2.4,2.2,6.8,5.3,7.4,4.6,4.8,6.3,6.5,8.8]#Salt Lake County Mental Health
dist_to_SLCUPD = [3.7,4.5,5.8,4.4,2.7,3.8,5.8,3.4,6.6,4,5.4,2.9,6.6,1.5,0.6,0,5.6,1.6,1.7,6.4,4.9,6.9,4.2,5.6,5.9,5.7,8.4]#Salt Lake County/United Police Dept
dist_to_WVP = [7.6,7.4,5.7,7.2,1.4,5.7,7.2,3.1,7.2,6.7,8.1,6.3,7.2,4,6.4,5.6,0,7.1,6.1,7.2,10.6,12,9.4,7.5,11.1,6.2,13.6]#West Valley Prosecutor
dist_to_HASLC = [2,6,4.1,5.3,0.5,1.9,7.7,5.1,5.9,2.3,6.2,1.2,5.9,3.2,2.4,1.6,7.1,0,1.6,4.9,3,5,2.3,5.5,4,5.1,5.2]#Housing Auth. of Salt Lake County
dist_to_UDMV = [3.6,5,3.6,6,1.7,1.1,6.6,4.6,5.4,1.8,6.9,1,5.4,3,2.2,1.7,6.1,1.6,0,4.4,4.6,6.6,3.9,6.5,5.6,4.3,6.9]#Utah DMV Administrative Office
dist_to_TDJC = [6.5,4.8,4.3,10.6,6.5,3.5,3.2,6.7,1,4.1,11.5,3.7,1,6.9,6.8,6.4,7.2,4.9,4.4,0,7.5,9.3,6.8,11.4,8.5,1.8,13.1]#Third District Juvenile Court
dist_to_CRSC = [1.9,9.5,3.3,5.9,3.2,4.9,11.2,8.1,8.5,3.8,6.9,4.1,8.5,6.2,5.3,4.9,10.6,3,4.6,7.5,0,2,2.9,6.4,2.8,6,4.1]#Cottonwood Regional Softball Complex
dist_to_HCO = [3.4,10.9,5,7.4,5.2,6.9,12.7,10.4,10.3,5.8,8.3,6.2,10.3,8.2,7.4,6.9,12,5,6.6,9.3,2,0,4.4,7.9,3.4,7.9,4.7]#Holiday City Office
dist_to_MCM = [2.4,8.3,6.1,4.7,2.5,4.2,10,7.8,7.8,4.3,4.1,3.4,7.8,5.5,4.6,4.2,9.4,2.3,3.9,6.8,2.9,4.4,0,4.5,1.7,6.8,3.1]#Murray City Museum
dist_to_VRSC = [6.4,6.9,9.7,0.6,6,9,8.2,4.2,11.5,7.8,0.4,6.9,11.5,4.4,4.8,5.6,7.5,5.5,6.5,11.4,6.4,7.9,4.5,0,5.4,10.6,7.8]#Valley Regional Softball Complex
dist_to_CCRS = [2.4,10,6.1,6.4,4.2,5.9,11.7,9.5,9.5,4.8,4.9,5.2,9.5,7.2,6.3,5.9,11.1,4,5.6,8.5,2.8,3.4,1.7,5.4,0,7,1.3]#City Center of Rock Springs
dist_to_RTPP = [5,4.4,2.8,10.1,5.4,3.5,5.1,6.2,2.8,3.2,11,3.7,2.8,6.4,6.5,5.7,6.2,5.1,4.3,1.8,6,7.9,6.8,10.6,7,0,8.3]#Rice Terrace Pavilion Park
dist_to_WHF = [3.6,13,7.4,10.1,5.5,7.2,14.2,10.7,14.1,6,6.8,6.4,14.1,10.5,8.8,8.4,13.6,5.2,6.9,13.1,4.1,4.7,3.1,7.8,1.3,8.3,0]#Wheeler Historic Farm

#creates a 2d array of distance between address locations
#O(1)
distance_2d_array = [dist_to_WGU, dist_to_IPG, dist_to_SHP, dist_to_TBHC, dist_to_SLCDHS, dist_to_SSLPW, dist_to_SLCSS, dist_to_DL, dist_to_SLCOH, dist_to_CL, dist_to_TCH, dist_to_SSLP, dist_to_CH, dist_to_RP, dist_to_SLCMH, dist_to_SLCUPD, dist_to_WVP, dist_to_HASLC, dist_to_UDMV, dist_to_TDJC, dist_to_CRSC, dist_to_HCO, dist_to_MCM, dist_to_VRSC, dist_to_CCRS, dist_to_RTPP, dist_to_WHF]


#creates a dictionary associating an addresss to a member location in the 2d distance array
#O(1)
address_dictionary = {}

address_dictionary["4001 South 700 East"] = 0 #Western Governors University
address_dictionary["1060 Dalton Ave S"] = 1 #International Peace Gardens
address_dictionary["1330 2100 S"] = 2 #Sugar House Park
address_dictionary["1488 4800 S"] = 3 #Taylorsville-Bennion Heritage
address_dictionary["177 W Price Ave"] = 4 #Salt Lake City Division of Health Services
address_dictionary["195 W Oakland Ave"] = 5 #South Salt Lake Public Works
address_dictionary["2010 W 500 S"] = 6 #Salt Lake City Streets and Sanitation
address_dictionary["2300 Parkway Blvd"] = 7 #Deker Lake
address_dictionary["233 Canyon Rd"] = 8 #Salt Lake City Ottinger Hall
address_dictionary["2530 S 500 E"] = 9 #Columbus Library
address_dictionary["2600 Taylorsville Blvd"] = 10 #Taylorsville City Hall
address_dictionary["2835 Main St"] = 11 #South Salt Lake Police
address_dictionary["300 State St"] = 12 #Council Hall
address_dictionary["3060 Lester St"] = 13 #Redwood Park
address_dictionary["3148 S 1100 W"] = 14 #Salt Lake County Mental Health
address_dictionary["3365 S 900 W"] = 15 #Salt Lake County/United Police Dept
address_dictionary["3575 W Valley Central Station bus Loop"] = 16 #West Valley Prosecutor
address_dictionary["3595 Main St"] = 17 #Housing Auth. of Salt Lake County
address_dictionary["380 W 2880 S"] = 18 #Utah DMV Administrative Office
address_dictionary["410 S State St"] = 19 #Third District Juvenile Court
address_dictionary["4300 S 1300 E"] = 20 #Cottonwood Regional Softball Complex
address_dictionary["4580 S 2300 E"] = 21 #Holiday City Office
address_dictionary["5025 State St"] = 22 #Murray City Museum
address_dictionary["5100 South 2700 West"] = 23 #Valley Regional Softball Complex
address_dictionary["5383 S 900 East #104"] = 24 #City Center of Rock Springs
address_dictionary["600 E 900 South"] = 25 #Rice Terrace Pavilion Park
address_dictionary["6351 South 900 East"] = 26 #Wheeler Historic Farm


#I have seperated the packages into 3 groups
#truck 1 packages all have 10:30 deadlines except 15 which must be delivered first before 9:00 (all 13 deliveres must take less than 2hours 30 mins)
#truck 2 packages 25, 28, 32, 6 delayed till 9:05, 25, 6 must be delivered by 10:30, 9 has wrong address
#truck 3 packages no special instructions and can be delivered by EOD

#load truck 1 with packages
#packages 1, 13, 14, 15, 16, 19, 20, 27, 29, 30, 31, 34, 37, 40 on truck 1
truck1_packages_id = [p1.package_id, p13.package_id, p14.package_id, p15.package_id, p16.package_id, p19.package_id, p20.package_id, p27.package_id, p29.package_id, p30.package_id, p31.package_id, p34.package_id, p37.package_id, p40.package_id]

#create truck 1 object
t1 = datetime.timedelta(hours=8, minutes=0)
truck1 = Truck(truck1_packages_id, "4001 South 700 East", 0, t1, 1)

#load truck 2 with packages
#packages 3, 6, 18, 25, 28, 32, 33, 35, 36, 38, 39 on truck 2
truck2_packages_id = [p3.package_id, p6.package_id,  p18.package_id, p25.package_id, p28.package_id, p32.package_id, p33.package_id, p35.package_id, p36.package_id, p38.package_id, p39.package_id]

#create truck 2 object
t2 = datetime.timedelta(hours=9, minutes=5)
truck2 = Truck(truck2_packages_id, "4001 South 700 East", 0, t2, 2)

#load truck 3 with packages
#packages 2, 4, 5, 7, 8, 9, 10, 11, 12, 17, 19, 21, 22, 23, 24, 26 on truck 3
truck3_packages_id = [p2.package_id, p4.package_id, p5.package_id, p7.package_id, p8.package_id, p9.package_id, p10.package_id, p11.package_id, p12.package_id, p17.package_id, p19.package_id, p21.package_id, p22.package_id, p23.package_id, p24.package_id, p26.package_id]

#create truck 3 object
t3 = datetime.timedelta(hours=12, minutes=0) #driver switches to truck 3 after early truck 1 packages delivered and starts time at end of truck 1 deliveries
truck3 = Truck(truck3_packages_id, "4001 South 700 East", 0, t3, 3)

print("truck1 packages: ", truck1_packages_id)
print("truck2 packages: ", truck2_packages_id)
print("truck3 packages: ", truck3_packages_id)

#runs the nearest neighbor function for the packages in each truck
packageDeliveryAlgoritm(truck1)
packageDeliveryAlgoritm(truck2)
packageDeliveryAlgoritm(truck3)



#creates a list containing all package ids
#O(1)
allPackages_id = [p1.package_id, p2.package_id, p3.package_id, p4.package_id, p5.package_id, p6.package_id, p7.package_id, p8.package_id, p9.package_id, p10.package_id, p11.package_id, p12.package_id, p13.package_id, p14.package_id, p15.package_id, p16.package_id, p17.package_id, p18.package_id, p19.package_id, p20.package_id, p21.package_id, p22.package_id, p23.package_id, p24.package_id, p25.package_id, p26.package_id, p27.package_id, p28.package_id, p29.package_id, p30.package_id, p31.package_id, p32.package_id, p33.package_id, p34.package_id, p35.package_id, p36.package_id, p37.package_id, p38.package_id, p39.package_id, p40.package_id]


#loops through all package ids on each truck and displays the mileage
#O(n)
for i in allPackages_id:
    package = packageHash.search(i)
    print("Package:", package.package_id, "Delivery Time:", package.time_delivered)

print("Truck 1 total mileage: ", truck1.mileage)
print("Truck 2 total mileage: ", truck2.mileage)
print("Truck 3 total mileage: ", truck3.mileage)
totalMileage = (truck1.mileage + truck2.mileage + truck3.mileage)
print("Total Miles: ", totalMileage)

#sets a time of 9:00 to check status of packages at this time
#O(1)
testTime1 = datetime.timedelta(hours=9, minutes=0)
testPackageDeliveryStatusMessage = ""

print("\nStatus of packages at", testTime1)

#loops through all packages to display status at 9:30
#O(n)
for i in allPackages_id:
    package = packageHash.search(i)

    packageDeliveryStatusMessage = ""

    if package.truckNumber == 1:
        if testTime1 <= t1:
            packageDeliveryStatusMessage = "at the Hub"
        elif testTime1 > t1 and testTime1 < package.time_delivered:
           packageDeliveryStatusMessage = "En Route"
        elif testTime1 >= package.time_delivered:
            packageDeliveryStatusMessage = "Delivered"
    if package.truckNumber == 2:
        if testTime1 <= t2:
            packageDeliveryStatusMessage = "at the Hub"
        elif testTime1 > t2 and testTime1 < package.time_delivered:
           packageDeliveryStatusMessage = "En Route"
        elif testTime1 >= package.time_delivered:
            packageDeliveryStatusMessage = "Delivered"
    if package.truckNumber == 3:
        if testTime1 <= t3:
            packageDeliveryStatusMessage = "at the Hub"
        elif testTime1 > t3 and testTime1 < package.time_delivered:
           packageDeliveryStatusMessage = "En Route"
        elif testTime1 >= package.time_delivered:
            packageDeliveryStatusMessage = "Delivered"
    print("Package:", package.package_id, "Status:", packageDeliveryStatusMessage)


#sets a time of 10:00 to check status of packages at this time
#O(1)
testTime1 = datetime.timedelta(hours=10, minutes=0)
print("\nStatus of packages at", testTime1)

#loops through all packages to display status at 10:00
#O(n)
for i in allPackages_id:
    package = packageHash.search(i)

    packageDeliveryStatusMessage = ""

    if package.truckNumber == 1:
        if testTime1 <= t1:
            packageDeliveryStatusMessage = "at the Hub"
        elif testTime1 > t1 and testTime1 < package.time_delivered:
           packageDeliveryStatusMessage = "En Route"
        elif testTime1 >= package.time_delivered:
            packageDeliveryStatusMessage = "Delivered"
    if package.truckNumber == 2:
        if testTime1 <= t2:
            packageDeliveryStatusMessage = "at the Hub"
        elif testTime1 > t2 and testTime1 < package.time_delivered:
           packageDeliveryStatusMessage = "En Route"
        elif testTime1 >= package.time_delivered:
            packageDeliveryStatusMessage = "Delivered"
    if package.truckNumber == 3:
        if testTime1 <= t3:
            packageDeliveryStatusMessage = "at the Hub"
        elif testTime1 > t3 and testTime1 < package.time_delivered:
           packageDeliveryStatusMessage = "En Route"
        elif testTime1 >= package.time_delivered:
            packageDeliveryStatusMessage = "Delivered"
    print("Package:", package.package_id, "Status:", packageDeliveryStatusMessage)

#sets a time of 12:30 to check status of packages at this time
#O(1)
testTime1 = datetime.timedelta(hours=12, minutes=30)
print("\nStatus of packages at", testTime1)

#loops through all packages to display status at 12:30
#O(n)
for i in allPackages_id:
    package = packageHash.search(i)

    packageDeliveryStatusMessage = ""

    if package.truckNumber == 1:
        if testTime1 <= t1:
            packageDeliveryStatusMessage = "at the Hub"
        elif testTime1 > t1 and testTime1 < package.time_delivered:
           packageDeliveryStatusMessage = "En Route"
        elif testTime1 >= package.time_delivered:
            packageDeliveryStatusMessage = "Delivered"
    if package.truckNumber == 2:
        if testTime1 <= t2:
            packageDeliveryStatusMessage = "at the Hub"
        elif testTime1 > t2 and testTime1 < package.time_delivered:
           packageDeliveryStatusMessage = "En Route"
        elif testTime1 >= package.time_delivered:
            packageDeliveryStatusMessage = "Delivered"
    if package.truckNumber == 3:
        if testTime1 <= t3:
            packageDeliveryStatusMessage = "at the Hub"
        elif testTime1 > t3 and testTime1 < package.time_delivered:
           packageDeliveryStatusMessage = "En Route"
        elif testTime1 >= package.time_delivered:
            packageDeliveryStatusMessage = "Delivered"
    print("Package:", package.package_id, "Status:", packageDeliveryStatusMessage)

#creates a menu to select options to display status of individual packages or to check truck miles or exit program
#O(1)
while(1):
    checkContinue = ''
    makeMenuChoice = int(input('\n Check Package Status (1) \n Check Truck Mileage (2) \n Exit Program (3)\n'))

    #check status of individual packages
    if makeMenuChoice == 1:
        while(checkContinue != 'n'):
            userPackageId = int(input('\n\nEnter a package id:\n'))

            #gets and hour and minutes from the user to check a specific time
            userTimeHour = int(input('Input hour:\n'))
            userTimeMinute = int(input('Input minutes\n'))

            userTime = datetime.timedelta(hours= userTimeHour, minutes= userTimeMinute)

            userPackage = packageHash.search(userPackageId)
            userPackageDeliveryStatusMessage = ""

            #sets the delivery status message depending on the user entered time
            if userPackage.truckNumber == 1:
                if userTime <= t1:
                    userPackageDeliveryStatusMessage = "at the Hub"
                elif userTime > t1 and userTime < userPackage.time_delivered:
                    userPackageDeliveryStatusMessage = "En Route"
                elif userTime >= userPackage.time_delivered:
                    userPackageDeliveryStatusMessage = "Delivered"
            if userPackage.truckNumber == 2:
                if userTime <= t2:
                    userPackageDeliveryStatusMessage = "at the Hub"
                elif userTime > t2 and userTime < userPackage.time_delivered:
                    userPackageDeliveryStatusMessage = "En Route"
                elif userTime >= userPackage.time_delivered:
                    userPackageDeliveryStatusMessage = "Delivered"
            if userPackage.truckNumber == 3:
                if userTime <= t3:
                    userPackageDeliveryStatusMessage = "at the Hub"
                elif userTime > t3 and userTime < userPackage.time_delivered:
                    userPackageDeliveryStatusMessage = "En Route"
                elif userTime >= userPackage.time_delivered:
                    userPackageDeliveryStatusMessage = "Delivered"


            print("\n\nUser Time:", userTime, "\nPackage:", userPackage.package_id, "       Status:", userPackageDeliveryStatusMessage, "\n  Delivery Time:", userPackage.time_delivered, "  Deadline:", userPackage.deadline, "\n  Address Delivered to: ", userPackage.street, userPackage.city, userPackage.state, userPackage.zip, "\n  Package Weight:", userPackage.weight, "\n  Special Notes:", userPackage.special_notes,  "\n  Truck Number:", userPackage.truckNumber)

            checkContinue = (input('Check another package(y/n)?'))

    #displays mileage
    if makeMenuChoice == 2:
        print("Truck 1 total mileage: ", truck1.mileage)
        print("Truck 2 total mileage: ", truck2.mileage)
        print("Truck 3 total mileage: ", truck3.mileage)
        totalMileage = (truck1.mileage + truck2.mileage + truck3.mileage)
        print("Total Miles: ", totalMileage)

    if makeMenuChoice == 3:
        break
