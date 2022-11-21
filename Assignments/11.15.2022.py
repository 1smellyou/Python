'''
# objects / classes
class personA:
    age = 56
    name = "Jack"
    height = 40
    lastname = "Birchwood"

person = personA()
print(person.name, person.lastname)

class Person:
    def __init__(self, age, name, height, lastname):
        self.age = age
        self.name = name
        self.height = height
        self.lastname = lastname

person1 = Person("56, Jack, 40, Birchwood")
if (person1.age> 21):
    print(person1.name, "is old enough to drink" )

person2 = Person("43, Bob, 34, cobblestone")

class bills:
    def __init__(self, rent, eletric, water, gas, phone):
        self.rent = rent
        self.eletric = eletric
        self.water = water
        self.gas = gas
        self.phone = phone

    def total(self):
        return(self.rent, self.eletric, self.water, self.gas, self.phone)

    def yearlytotal(self):
        return self.total() * 12

jackbills = bills(1350, 258, 100, 0, 115)
jackstotal = jackbills.total()
print(jackstotal)
print(jackbills.yearlytotal())

class pizza:
    def __init__(this, size, crust, toppings):
        this.size = size
        this.crust = crust
        this.toppings = toppings

pizza = pizza("large", "stuffed", ["pepperoni", "jalapeno"])
print(pizza.toppings)
'''
file = open("test.text", "r")
print(file.read())
file.seek(0, 0)
print(file.read(4))

print(file.readline())
print(file.readline())
file.close()

f = open("test.txt", "w")
f.write("omg i created a file!\n")
f.close()

f = open("test.txt", "a")
f.write("hey, look another line\n")
f.write("adding anothor one!\n")
f.close()

def fileexists(filename):
    try:
        f = open(filename, "x")
        f.close()
        return True
    except:
        return False

print("Enter filename:")
filename = input()

if fileexists(filename) == False:
    print("File exists, what would you like to add")
    usertext = input()
    f = open(filename, "a")
    f.write(usertext)
    f.close()
else:
    print("Creating new file, add some text:")
    usertext = input()
    f = open(filename, "w")
    f.write(usertext + "\n")
    f.close()

    f = open(filename, 'r')
    f.read()
    f.close()



