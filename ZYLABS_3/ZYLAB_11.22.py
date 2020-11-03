# Katheryn Busch PSID: 1868948
x = input()

x = x.split(" ")

y = {}

for each in x:
    if each in y:
        y[each] = y[each] + 1
    else:
        y[each] = 1

for each in x:
    print(each, y[each])