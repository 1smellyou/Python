# assignment
# display 3 properties
# allow the user to change one of the properties using the key
# system will generate a random property and display all 3 properties again

''' initial properties will be randomly generated
1 Slash 905
2 Fire damage 674
3 Poison affect 67

Which property would you like to change?

1 Speed attack 900
2 Protection 1068
3 Healing 89

loop until user is happy
'''

'''
git commands to save files
1. make sure you are in root python folder
2. git status - tell us about any changes in our dictionary
3. git add [file] - add file to our list of items to be connected
4. git status - should show all our changes in green
5. git commit -m "message for commit"
6. git push - sends the data
'''
from random import randint


powers = {1:'Slash 905', 2:'Fire damage 674', 3:'Poison affect 67'}

for power in powers:
    print(power,powers[power])

extrapowers = {1 :'Speed attack 900' , 2:'Protection 1068', 3:'Healing 89'}
print('Which of these would you like to change?')
choice = input()
random = randint(1,3)
randompower = extrapowers[random]

powers[int(choice)] = randompower

for power in powers:
    print(power,powers[power])


'''
properties = powers

print(powers[0])
x = powers
while (x < 3):
    print("Which property would you like to change?")
question = input()
randomproperty = randint(1,3)
print(powers[randomproperty])

def getproperties(powers):
    propertiesToreturn = []
    i = 0
while i < propertiesToreturn.append(randint(1,65)):
      i = i + 1 
return propertiesToreturn
propertiesToreturn = powers

y = properties
powers = ['1 Speed attack 900', '2 Protection 1068', '3 Healing 89']
while (y < 3):
    print("Which of these will you use?")
    question = input()
    print(properties[0])

'''
