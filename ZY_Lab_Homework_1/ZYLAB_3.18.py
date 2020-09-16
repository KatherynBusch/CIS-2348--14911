
wallHeight = int(input("Enter wall height (feet):\n"))

wallWidth = int(input("Enter wall width (feet):\n"))

wallArea = wallHeight * wallWidth

print("Wall area: "+str(wallArea)+" square feet")

paintNeeded = wallArea/350

print("Paint needed: %.2f gallons"%(paintNeeded))

cans = round(paintNeeded)
print("Cans needed:",cans, "can(s)\n")


paint = {'red': 35, 'blue':25, 'green': 23}

paintColor = str(input('Choose a color to paint the wall:\n'))

print("Cost of purchasing "+ paintColor +" paint: $"+str(cans*paint[paintColor]))




