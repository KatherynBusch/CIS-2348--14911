# Katheryn Busch PSID: 1868948
davyMenu = """Davy's auto shop services
Oil change -- $35
Tire rotation -- $19
Car wash -- $7
Car wax -- $12"""
print(davyMenu)
# dictionary for the auto shop services
dict1 = {"Oil change":35,"Tire rotation":19,"Car wash":7,"Car wax":12,"-":"No service"}

print("\nSelect first service:\n",end="")
service_1 = input()
print("Select second service:\n",end="")
service_2 = input()

print("\nDavy's auto shop invoice\n")
# Output for choice of service 1 or 2
if service_1!='-' and service_2!='-':
    print("Service 1: "+service_1+", $"+ str(dict1[service_1]))
    print("Service 2: "+service_2+", $"+ str(dict1[service_2]))
    Total = dict1[service_1]+dict1[service_2]
elif service_1=='-':
    print("Service 1: "+"No service")
    print("Service 2: "+service_2+", $"+ str(dict1[service_2]))
    Total = dict1[service_2]
else:
    print("Service 1: "+service_1+", $"+ str(dict1[service_1]))
    print("Service 2: "+"No service")
    Total = dict1[service_1]

print("\nTotal: $"+str(Total))