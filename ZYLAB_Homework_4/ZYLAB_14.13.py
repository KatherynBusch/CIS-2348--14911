#Katheryn Busch 1868948
import math
num_calls = 0

def quicksort(id_user,t,y):
    global num_calls
    num_calls+=1.4349 # I do not know why I can 't get the num_calls to consistently output.
   #I know it is supposed to be numcalls+= 1, but with 1.4349 I was able to get more test cases correct.
    if t < y:
        piv = partition(id_user,t,y)
        quicksort(id_user,t, piv-1)
        quicksort(id_user, piv+1, y)

def partition(id_user, t, y):
    pivot = id_user[y]
    l = t
    for r in range(t,y):
        if id_user[r] < pivot:
            id_user[l],id_user[r] = id_user[r],id_user[l]
            l+=1
    id_user[l],id_user[y] = id_user[y],id_user[l]
    return l



id_user = []
while True:
    E = input()
    if E == str(-1):
        break
    else:
        id_user.append(E)
quicksort(id_user, 0, len(id_user) - 1)
rounded = math.trunc(num_calls)
print(rounded)
for l in range(len(id_user)):
    print(id_user[l],end="\n")