'''
# How do call for a function to be used
#print("a string")

def print2(words = 'no words '):
    print(words * 2)

print2("big words ")

list = []
'''
# ask user for their email or phone number
# keep gorcery list from user
# make sure i have an empty list
# use a while loop to keep collecting groceries
# ask user if they are done to exit loop, maybe look for a keyword in the input to stop the loop
# print full list when they are done
# save it to a file, send a text message, send an email...

# while their answer is yes
    # ask for another item
def getGroceryItem ():
    print("What do you want to add to your list?")
    item = input()

def print2(words = 'no words'):
    print2(words * 2)

print2("big words")

receiptList = []

users = {"Bazinga": "Sheldon", "Poya": "Kirby", "Pika": "Pikachu"}

def greetuser ( username):
    fullname = users[username]
    global tempname
    tempname = fullname
    return fullname

name = greetuser("Bazinga")

print(tempname)

print("Enter the password") 
password = input()
print("password:" + password)

def getuser (username):
    fullname = users[username]
    return fullname

def login():
    print("Enter your user name:")
    username = input()
    return username

def checkuser (username):
    if username in users:
        return True
    else:
        return False

user = login()
validuser = checkuser(user)
if validuser == True:
   print("Welcome " + getuser(user))

loggedIn = False
while loggedIn == False:
    user = login()
    validuser = checkuser(user)
    if validuser:
        loggedIn = True
        print("Welcome " + getuser(user))
    else:
        print("Mawhaha, login failed")


