from operator import truediv


users = {"Bob": "Steven",  "Alice": "Walter",  "Dean": "Edward"}
tempname = "" # globel string

def greetuser ( username):
    fullname = users[username]
    # print (fullname)
    global tempname 
    tempname = fullname
    return fullname

# for some reason we have the user name, maybe they logged in?
name = greetuser("Dean")
#print ("Welcome " + name + "!")



print(tempname)

# do functions with optional parameter/agument
def optional (firstname, lastname = ""):
    print("Hello" + firstname + " " + lastname)
    return

optional("John", "Doe")
optional("Mark") 



# take in data
print("Enter the password")
password = input()
print("Password:" + password)

def getuser (username):
    fullname = users[username]
    return fullname


def login():
    print("Enter you user name:")
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
    print("Hello " + getuser(user))








 # random number functions

# homework
''' Using the login above, use a while loop
to make the system keep asking for a username until
the user provides a username from your list'''