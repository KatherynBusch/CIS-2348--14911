# Katheryn Busch PSID: 1868948
partsData = input().split()
firstName = partsData[0]
while firstName != '-1':
    try:
        age = int(partsData[1]) + 1
    except ValueError:
        age = 0
    print('{} {}'.format(firstName, age))

    partsData = input().split()
    firstName = partsData[0]