from random import choice, randint


def clearFile():
    filename = 'test.csv'
    f = open(filename, 'w')
    f.close() 
def getRandomNumber():
    randomNumber = randint(1,1000)
    return str(randomNumber)
def getRandomName():
    names = ["Mario", "George", "Sheldon", "Edward", "Donald", "Oliva", "Alice",
     "Amy", "Fred", "Leo", "Rick", "Mark", "Walter", "Susan", "Hanna", "Jack",
      "Isa", "John", "Penny", "Stacy", "Sam", "Dean", "Nicole", "Tom", "Jerry"]
    return choice(names)


clearFile()
x = 0
#randomNumber = 0
#while (randomNumber > 30):
while (x < 25):
    x += 1 
 #   print (x) 
    #print(getRandomNumber())
    #print("John", ",", "56", ",", "47", ",", "190", ",", "176", ",", "1000")
    f = open("test.csv", "a")
    f.write(getRandomName() + "," + getRandomNumber() + "," + getRandomNumber() +
     "," + getRandomNumber() + "," + getRandomNumber() + "," +
      getRandomNumber() + "\n")
    f.close()
