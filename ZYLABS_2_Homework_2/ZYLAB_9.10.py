# Katheryn Busch PSID: 1868948
# Coding Problem #2 CIS 2348 Homework 2
import csv

fileName = input()
wordF = {}

with open(fileName, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for i in csvreader:
        for word in i:
            if word not in wordF.keys():
                wordF[word] = 1
            else:
                wordF[word] += 1

for key in wordF.keys():
    print(key + " " + str(wordF[key]))