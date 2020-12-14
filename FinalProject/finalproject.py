#Katheryn Busch PSID: 1868948
import csv
from datetime import datetime
from datetime import date

#set current date
dt = datetime.combine(date.today(), datetime.min.time())

# Class for methods used to create output inventory files


# reading data from pricelist.csv and sorting it based on item_ID
f1 = open("../PriceList.csv", "r")
data1 = csv.reader(f1)
data1 = list(data1)
data1.sort(key=lambda l: l[0])



# reading data from ManufacturerList.csv and sorting it based on item_ID
f2 = open("../ManufacturerList.csv", "r")
data2 = csv.reader(f2)
data2 = list(data2)
data2.sort(key=lambda l: l[0])


# reading data from serviceDatesList.csv  and sorting it based on item_ID
f3 = open("../ServiceDatesList.csv", "r")
data3 = csv.reader(f3)
data3 = list(data3)
data3.sort(key=lambda l: l[0])


# creating list to store each column seprately in list
item_ID = []
manufacturer_name = []
item_type = []
price = []
service_dates = []
is_damaged = []


#fill lists with correct info from input files
for row in data1:
    item_ID.append(row[0])
    price.append(row[1])

for row in data2:
    manufacturer_name.append(row[1])
    item_type.append(row[2])
    is_damaged.append(row[3])

for row in data3:
    service_dates.append(row[1])


# class created for the Inventory which will create all the reuired output files
class Inventory:
    data_csv = []

    # constructor for the class
    def __init__(self, item_ID, manufacturer_name, item_type, price, service_dates, is_damaged):
        self.item_ID = item_ID
        self.manufacturer_name = manufacturer_name
        self.item_type = item_type
        self.price = price
        self.service_dates = service_dates
        self.is_damaged = is_damaged

    # method for creating fullinventory.csv
    def create_fullinventory(self):
        file = open("../FullInventory.csv", "w")
        #add data into list
        data = [self.item_ID, self.manufacturer_name, self.item_type, self.price, self.service_dates, self.is_damaged]

        for x, y, z, a, b, c in zip(*data):
            self.data_csv.append([x, y, z, a, b, c])
        #sort by manufacturer name
        self.data_csv.sort(key=lambda l: l[1])

        #write to the file
        writer = csv.writer(file)

        for d in self.data_csv:
            writer.writerow(d)
    #debugging tool used for error checking
    def debug(self):
        print("Item Id")
        print(self.item_ID)
        print("Price")
        print(self.price)
        print("Item type")
        print(self.item_type)
        print("Damged")
        print(self.is_damaged)
        print("Manufacturer Name")
        print(self.manufacturer_name)
        print("Service Date")
        print(self.service_dates)
    #creates 3 output files
    def create_itemtypeinventory(self):
        file1 = open("../Laptop.csv", "w+")
        file2 = open("../Phone.csv", "w+")
        file3 = open("../Tower.csv", "w+")
        ''' Each row of the file should contain
        item ID, manufacturer name, price, service date, and list if it is damaged. The items
        should be sorted by their item ID. '''

        data = [self.item_ID, self.manufacturer_name, self.item_type, self.price, self.service_dates, self.is_damaged]
        newData = []
        for x, y, z, a, b,c in zip(*data):
            newData.append([x, y, z, a, b,c])
        #sort by Item ID
        newData.sort(key=lambda l: l[0])
        #create three csv.writer's for each file
        writer1 = csv.writer(file1)
        writer2 = csv.writer(file2)
        writer3 = csv.writer(file3)

        for d in newData:

            if d[2] == "laptop":
                d.remove(d[2]) #make sure to remove the item type from the output
                #write to file
                writer1.writerow(d)

            elif d[2] == "phone":
                d.remove(d[2])
                writer2.writerow(d)


            elif d[2] == "tower":
                d.remove(d[2])
                writer3.writerow(d)


            else:
                continue





    def create_pastservicedateinventory(self):
        file = open("../PastServiceDateInventory.csv", "w+")

        data = [self.item_ID, self.manufacturer_name, self.item_type, self.price, self.service_dates, self.is_damaged]
        newData = []
        for x, y, z, a, b, c in zip(*data):
            newData.append([x, y, z, a, b, c])
        #sort each value by date
        newData.sort(key=lambda l: datetime.strptime(l[4], '%m/%d/%Y'))

        #grab the current date
        dt = datetime.combine(date.today(), datetime.min.time())

        writer = csv.writer(file)

        for d in newData:
            #If the item service date is past the current date then write it onto the file
            if datetime.strptime(d[4], '%m/%d/%Y') < dt:
                writer.writerow(d)





    def create_damagedinventory(self):
        file = open("../DamagedInventory.csv", "w+")

        data = [self.item_ID, self.manufacturer_name, self.item_type, self.price, self.service_dates, self.is_damaged]
        newData = []
        for x, y, z, a, b, c in zip(*data):
            newData.append([x, y, z, a, b, c])

        #sort by price, make sure to change string to int and reverse the sorting order
        newData.sort(key=lambda l: int(l[3]), reverse = True)

        writer = csv.writer(file)

        for d in newData:
            #if the item is damaged then add the item to the damage file
            if d[5] == "damaged":
                d.remove(d[5]) #make sure to remove the damage label from the output file
                writer.writerow(d)
    #this function retrieves the items for Part 2
    def retrieveQuery(self, item, type):
        data = [self.item_ID, self.manufacturer_name, self.item_type, self.price, self.service_dates, self.is_damaged]
        newData = []

        correctItems = [] #this list contatins matching items that aren't damaged nor past the service date
        for x, y, z, a, b, c in zip(*data):
            newData.append([x, y, z, a, b, c])

        #set current date to the variable
        dt = datetime.combine(date.today(), datetime.min.time())

        for i in newData:
            #if both the item and type that the user provided matches
            if item.lower() == i[1].lower() and type.lower() == i[2].lower():

                #before we can add this item, we must check if the item is not damaged nor past due date
                if i[5].lower() != "damaged" and dt < datetime.strptime(i[4], '%m/%d/%Y')  :
                    correctItems.append(i)

        #if there's only one valid item then print that one
        if len(correctItems) == 1:
            print("Your item is: " + correctItems[0][0] + ", " + correctItems[0][1] + ", " + correctItems[0][2] + ", aat $" + correctItems[0][3])
        #if there's no valid items print the error prompt
        elif len(correctItems) == 0:
            print("No such item in inventory")
        #if there's more than 1 valid item then sort by price and print the first two
        else:
            correctItems.sort(key=lambda l: int(l[3]), reverse=True)
            print("Your item is: " + correctItems[0][0] + ", " + correctItems[0][1] + ", " + correctItems[0][
                2] + ", and $" + correctItems[0][3])
            print("You may, also, consider: " + correctItems[1][0] + ", " + correctItems[1][1] + ", " + correctItems[1][
                2] + ", and $" + correctItems[1][3])









#continuously ask the user to construct part 1 and 2
while True:
    result = input("Press 1 for the Processed Inventory Reports and 2 for the Interactive Inventory Query Capability. Press any other key to quit: ")

    # creating object
    ob = Inventory(item_ID, manufacturer_name, item_type, price, service_dates, is_damaged)

    # calling methods to create fullinventory.csv
    #if the user presses 1, create the output files
    if result == "1":
        ob.create_fullinventory()
        ob.create_itemtypeinventory()
        ob.create_pastservicedateinventory()
        ob.create_damagedinventory()
        print("All output files have successfully been created.")
    #if the user presses 2, retrieve the given items from the query
    elif result == "2":
        while True:
            # prompt the user for the query
            query = input("Type a query or q to quit: ")
            #query = "I want a Lenovo Tower"
            # if the user enters q exit the program
            if query == "q":
                break
            # intialize the manufacturer and type
            # ASSUMING THESE ARE THE ONLY VALID ITEMS AND TYPES
            validItems = ["apple","dell","lenovo","samsung"]
            validTypes = ["phone","laptop","tower"]

            item = ""
            types = ""
            #create booleans to make sure only one item and type are given in a user query
            onlyOneIteminQuery = True
            onlyOneTypeinQuery = True
            for i in validItems:
                for j in query.split():
                    #if the item matches a valid item,
                    if i.lower() == j.lower():

                        #check if this the the first time a valid item was found in the query
                        if onlyOneIteminQuery == True:
                            item = i.lower()
                            onlyOneIteminQuery = False

                        else:
                            #if this wasn't the first time then the user did an invalid query so delete the results
                            item = ""
                            break



            #repeat same process, this time with types
            for i in validTypes:
                for j in query.split():
                    if i.lower() == j.lower():

                        if onlyOneTypeinQuery == True:
                            types = i.lower()
                            onlyOneTypeinQuery = False
                        else:

                            types = ""
                            break

            #retrieve results
            ob.retrieveQuery(item,types)
    else:
        print("Goodbye!")
        break


