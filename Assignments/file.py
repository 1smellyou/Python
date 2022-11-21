print("Enter filename:")
filename = input()

def fileexists(filename):
    try:
        f = open(filename, "x")
        f.close()
        return True
    except:
        return False

if fileexists(filename) == False:
    print("File exists, what would you like to add")
    usertext = input()
    f = open(filename, "a")
    f.write(usertext + "\n")
    numbers = ['1','2','3','4']
    for num in numbers:
        f.write(num + "\n")
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

'''
file = open("test.text", "r")
print(file.read())
file.seek(0, 0)
print(file.read(4))

print(file.readline())
print(file.readline())
file.close()

f = open("test.txt", "w")
f.write("2, 4, 6, 8, 10, 12, 14, 16,\n")
f.close()

f = open("test.txt", "a")
f.write("18, 20, 22, 24, 26, 28, 30, 32\n")
f.write("5, 10, 15, 20, 25, 30, 35, 40\n")
f.close()
'''
