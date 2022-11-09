# random number functions 
# if statements 
# boolean values
Mynumber = 226
evenNumberList = ["0", "2", "4", "6", "8"]

def modIsEven(num):
    modValue = num % 2
    if modValue > 0:
          return False
    return True

def isEven(num):
    mynum = str(num)
    #print(mynum[-1])
    lastDigit = mynum[-1]
    if lastDigit in evenNumberList:
         return True
    return False

print(modIsEven(Mynumber))
print(isEven(Mynumber))


evenNumberList = ["0", "2", "4", "6", "8"]
Mynumber = 17
def isEven(num):
    print(str(Mynumber[-1]))

    mynum = str(num)
    print(mynum[-1])
    lastDigit = mynum[-1]
    if lastDigit in evenNumberList:
       return True
    return False

print(isEven(Mynumber))

modValue = Mynumber % 2
print(Mynumber % 2)

from random import randint

name = "Joal"
while (name != "Sheldon") and (name != "Howard"):
     print("Your not one of my friends!")

age = 14

if age < 21:
    cantSmoke = True
elif age < 65:
      cantsmoke = False
else: 
    cantSmoke = True


messages = { 1 : "Not Today", 2 : "Try again later", 3 : "Definitely Not!", 4 : "There's a chance", 5 : "Yes" }

print("What's your question?")
question = input()
randomNumber = randint(1,5)
#print(randomNumber)
print(messages[randomNumber])


def getNumbers(numbers):
    numbersToReturn = []
    i = 0
    while i < numbersToReturn.append(randint(1,65)):
        i = i + 1 # shorthand version: i += 1
    return numbersToReturn

def playpowerball():
    print("Here are your lucky numbers:")
    numbers = getNumbers(5)
    print(numbers)

playpowerball()