print("Enter filename: ")
filename = input()

def fileexists(filename):
    try:
        f = open(filename, "w")
        f.close()
        return True
    except:
        return False

if fileexists(filename) == False:
    print("This file exists, what would you add?")
    usertext = input()
    f = open(filename, "a")
    f.write(usertext + "\n")
    numbers = ['1', '2', '3', '4']
    for num in numbers:
        f.write(num + "\n")
    f.close()
else:
    print("Creating this file, write something in your text")
    usertext = input()
    f = open(filename, "w")
    f.write(usertext + "\n")
f.close()

f = open(filename, 'r')
f.read()
f.close