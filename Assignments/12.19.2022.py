name = 'Mark'
age = 38

print(name + ' is ' + str(age) + ' a youtuber!')
print(name, 'is' + str(age), 'a youtuber!')
print(f"{name} 'is'{age} 'a youtuber!'")

class User:
    first_name = None
    last_name = None

    def __init__(this, first, last):
        this.first_name = first
        this.last_name = last

    def get_name(this):
        return f"{this.first_name} {this.last_name}"

def __get_length(thism, data):
    return len(data)

user = User("Steve", "Trevor")
print(f"{user.get_name()} was a character in DC comics.")

first_name = ''
def get_first_name():
    print(first_name)

class PingPong:
    ball = 0

VELOCITY = 3.14
NUMBER_PLAYERS = 2


