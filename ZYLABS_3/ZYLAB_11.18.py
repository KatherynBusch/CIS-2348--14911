# Katheryn Busch PSID: 1868948
integers = input().split()

non_neg=[]

for x in integers:

    x = int(x)

    if x >= 0:

        non_neg.append(x)

non_neg.sort()

for j in non_neg:

    print(j, end=' ')