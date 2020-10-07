# Katheryn Busch PSID: 1868948
# Coding Problem #2 CIS 2348 Homework 2
q = int(input())
w = int(input())
e = int(input())
r = int(input())
t = int(input())
a = int(input())

solution_found = False

for x in range(-10, 11):
    for y in range(-10, 11):
        if q * x + w * y == e and r * x + t * y == a:
            print(x, y)
            solution_found = True

if not solution_found:
    print("No solution")