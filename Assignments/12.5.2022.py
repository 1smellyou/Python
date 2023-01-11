class Total:    # class name
    # the following items are the properties of the class
    Iron = 0
    Emerald = 0
    Copper = 0
    Amethyst = 0
    Gold = 0
    Coal = 0
    Flint = 0
    Diamonds = 'y'
    Crystal = 'n'

    # Class constructor - this is assigns the given variables to the 'properties' of our object
    def __init__(this, iron, emerald, copper, amethyst, gold, coal, flint, diamonds = 'y', crystal = 'n'):
        this.Iron = iron
        this.Emerald = emerald
        this.Copper = copper
        this.Amethyst = amethyst
        this.Gold = gold
        this.Coal = coal
        this.Flint = flint
        this.Diamonds = diamonds
        this.Crystal = crystal

    # a function that the house class can do
    def UpdateTotal(this, iron, emerald, copper, amethyst, gold, coal, flint, diamonds, crystal):
        # Save these values to the database
        print("saving to the database")

donaldsMinerals = Total( 56, 20, 78, 40, 36, 190, 45, 'y', 'n')
#print("Bolis house is: ", bolisHouse.SquareFootage, "sqFt")

isasMinerals = Total(90, 123, 74, 80, 24, 45, 145, 'n', 'n')           # Here we are creating instances of the class
edwardsMinerals = Total( 87, 3, 47, 58, 46, 127, 90, 'y', 'n')
gabrielsminerals = Total(129, 56, 23, 45, 45, 57, 67, 'y', 'y')
laxsminerals = Total (67, 34, 87, 90, 65, 45, 78, 'n', 'y')

members = [donaldsMinerals, isasMinerals, edwardsMinerals, gabrielsminerals, laxsminerals] # adding them to a list

for member in members:        # looping through our list of house objects
    if member.Iron > 40:
        print(member.Iron, "You may keep some of your minerals!")
    if member.Copper < 50:
        print(member.Copper, 'You have earned a box of minerals!')
