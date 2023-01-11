# 5 contacts
# name, phone, address, birth, age, city, state, zipcode, email, id, criminal records, passports, car plate, bills, job, 
# use csv
import os
clear = lambda: os.system('cls')

class Contact:

    Name = 0
    Phone = 0
    Id = 0

    def __init__(this, name = "", phone = "", id = ""):
        this.Name = name
        this.Phone = phone
        this.Id = id

    def save(this):
        filename = 'contact.csv'
        f = open(filename, 'a')
        f.write(f"{this.Name},{this.Phone}\n")
        f.close() 

    def clear_contacts(this):
        filename = 'contact.csv'
        f = open(filename, 'w')
        f.close()
    def pause(this):
        input("Press enter to continue")
        clear()

    def delete_contact(this, id):
        contacts = this.get_contacts()
        for contact in contacts:
            print(contact.Id,contact.Name)
        contact_id = input("Which contact do you want to delete? ")
        f = open("contact.csv", 'w')
        f.close()
        for contact in contacts:
            if contact.Id != contact_id:
                contact.save()
        this.pause()

    clear()
    def get_contacts(this):
        filename = 'contact.csv'
        f = open(filename,"r")
        number_lines = len(f.readlines())
        f.seek(0,0)
        starting_line = 0
        contacts = []
        while starting_line < number_lines:
            line = f.readline()
            line = line.strip()
            pieces = line.split(",")
            name = pieces[0]
            phone = pieces[1]
            contact = Contact(name, phone, str(starting_line + 1))
            contacts.append(contact)
            starting_line += 1
        return contacts

clear()
def show_contacts():
    print("Showing contacts")
    print()
    filename = 'contact.csv'
    f = open(filename,"r")
    number_lines = len(f.readlines())
    f.seek(0,0)
    starting_line = 0
    while starting_line < number_lines:
        line = f.readline()
        line = line.strip()
        pieces = line.split(",")
        name = pieces[0]
        phone = pieces[1]
        contact = Contact(name, phone)
        print(contact.Name, contact.Phone)
        starting_line += 1

    f.close()







choice = "0"
while choice != "6":
    print("1. Add a contact")
    print("2. Show contacts")
    print("3. Edit a contact")
    print("4. Delete contact")
    print("5. Clear contacts")
    print("6. Exit")
    choice = input()
    clear()
    if choice == "1":
        print("Please enter your name")
        name = input()
        print("Please put your phone number")
        phone = input()
        contact = Contact(name, phone)
        contact.save()
        print("Your contact is saved")
        clear()
    if choice == "5":
        print("Are you sure you want to clear (y/n)")
        answer = input()
        if answer == "y":
            contact = Contact()
            contact.clear_contacts()
    if choice == "2":
        show_contacts()
        print()
        input("Press enter to continue")
        clear()
    if choice == "3":
        print("Which contact would you like to change")
        print()
    if choice == "4":
        contact = Contact()
        contact.delete_contact(1)

''''
from random import choice, randint


def clearFile():
    filename = 'contact.csv'
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
'''