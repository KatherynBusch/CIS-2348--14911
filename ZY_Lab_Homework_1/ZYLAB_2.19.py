lemon = float(input('Enter amount of lemon juice (in cups):\n'))
water = float(input('Enter amount of water (in cups):\n'))
agave = float(input('Enter amount of agave nectar (in cups):\n'))
servings = float(input('How many servings does this make?\n'))


print('\nLemonade ingredients - yields ''{:.2f}'.format(servings), 'servings')
print('{:.2f}'.format(lemon), 'cup(s) lemon juice')
print('{:.2f}'.format(water), 'cup(s) water')
print('{:.2f}'.format(agave), 'cup(s) agave nectar\n')


desiredNumberOfServings = float(input('How many servings would you like to make?\n'))

print('\nLemonade ingredients - yields', '{:.2f}'.format(desiredNumberOfServings), 'servings')
serving = desiredNumberOfServings / servings

lemon = lemon * serving
water = water * serving
agave = agave * serving

print('{:.2f}'.format(lemon), 'cup(s) lemon juice')
print('{:.2f}'.format(water), 'cup(s) water')
print('{:.2f}'.format(agave), 'cup(s) agave nectar\n')


print('Lemonade ingredients - yields','{:.2f}'.format(desiredNumberOfServings), 'servings')
lemonGalllon = lemon / 16
waterGallon = water / 16
agaveGallon = agave / 16

print('{:.2f}'.format(lemonGalllon), 'gallon(s) lemon juice')
print('{:.2f}'.format(waterGallon), 'gallon(s) water')
print('{:.2f}'.format(agaveGallon), 'gallon(s) agave nectar')