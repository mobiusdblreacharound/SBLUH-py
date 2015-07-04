def main(isInit):
    firstName = raw_input("Enter First Name: ")
    firstNameUpper = firstName.upper()
    print
    lastName = raw_input("Enter Last Name: ")
    lastNameUpper = lastName.upper()

    firstNameConverted = calc(firstName)
    lastNameConverted = calc(lastName)

    if isInit == False:
        print "You are the " + sbluhClass(firstNameConverted) + " of " + sbluhAspect(lastNameConverted) + "."
    else:
        return {"class": sbluhClass(firstNameConverted), "aspect": sbluhAspect(lastNameConverted)}

def calc(input):
    data = input
    data = data.upper()
    inputUpper = data
    beginConvert = [ inputUpper[0] ]
    finalStuff = listAspect(beginConvert)

    return finalStuff

def sbluhClass(input):
    if input == 2 or input == 3:
        return "Maid"
    elif input == 4 or input == 5:
        return "Mage"
    elif input == 6 or input == 7:
        return "Witch"
    elif input == 8 or input == 9:
        return "Knight"
    elif input == 10 or input == 11:
        return "Thief"
    elif input == 12 or input == 13:
        return "Blacksmith"
    elif input == 14 or input == 15:
        return "Citizen"
    elif input == 16 or input == 17:
        return "Rogue"
    elif input == 18 or input == 19:
        return "Runner"
    elif input == 20 or input == 21:
        return "Heir"
    elif input == 22 or input == 23:
        return "Seer"
    elif input == 24 or input == 25:
        return "Slayer"
    elif input == 26 or input == 27:
        return "Magician"
    elif input == 28 or input == 29:
        return "Bard"
    elif input == 30 or input == 31:
        return "Scout"
    elif input == 32 or input == 33:
        return "Archer"
    elif input == 34 or input == 35:
        return "Runner"
    elif input == 36 or input == 37:
        return "Seer"
    elif input == 38 or input == 39:
        return "Sylph"
    elif input == 40 or input == 41:
        return "Prince"
    elif input == 42 or input == 43:
        return "Alchemist"
    elif input == 44 or input == 45:
        return "Keeper"
    elif input == 46 or input == 47:
        return "Jester"
    elif input == 48 or input == 49:
        return "Muse"
    elif input == 50 or input == 51:
        return "Lord"
    elif input == 52:
        return "Waste"
    else:
        return "Glitch"

def sbluhAspect(input):
    if input == 2 or input == 3:
        return "Heart"
    elif input == 4 or input == 5:
        return "Energy"
    elif input == 6 or input == 7:
        return "Dimension"
    elif input == 8 or input == 9:
        return "Light"
    elif input == 10 or input == 11:
        return "Flow"
    elif input == 12 or input == 13:
        return "Void"
    elif input == 14 or input == 15:
        return "Rhythm"
    elif input == 16 or input == 17:
        return "Space"
    elif input == 18 or input == 19:
        return "Infinity"
    elif input == 20 or input == 21:
        return "Quanta"
    elif input == 22 or input == 23:
        return "Mind"
    elif input == 24 or input == 25:
        return "Doom"
    elif input == 26 or input == 27:
        return "Rage"
    elif input == 28 or input == 29:
        return "Information"
    elif input == 30 or input == 31:
        return "Hope"
    elif input == 32 or input == 33:
        return "Flame"
    elif input == 34 or input == 35:
        return "Constellations"
    elif input == 36 or input == 37:
        return "Blood"
    elif input == 38 or input == 39:
        return "Electricity"
    elif input == 40 or input == 41:
        return "Breath"
    elif input == 42 or input == 43:
        return "End"
    elif input == 44 or input == 45:
        return "Earth"
    elif input == 46 or input == 47:
        return "Heart"
    elif input == 48 or input == 49:
        return "Time"
    elif input == 50 or input == 51:
        return "Water"
    elif input == 52:
        return "0x000F"
    else:
        return "Error"

def listAspect(namelist):
    a = namelist[0]
    a = a.upper()
    # i'm sorry this is really really bad but it works
    if a == 'A':
        return 1
    elif a == 'B':
        return 2
    elif a == 'C':
        return 3
    elif a == 'D':
        return 4
    elif a == 'E':
        return 5
    elif a == 'F':
        return 6
    elif a == 'G':
        return 7
    elif a == 'H':
        return 8
    elif a == 'I':
        return 9
    elif a == 'J':
        return 10
    elif a == 'K':
        return 11
    elif a == 'L':
        return 12
    elif a == 'M':
        return 13
    elif a == 'N':
        return 14
    elif a == 'O':
        return 15
    elif a == 'P':
        return 16
    elif a == 'Q':
        return 17
    elif a == 'R':
        return 18
    elif a == 'S':
        return 19
    elif a == 'T':
        return 20
    elif a == 'U':
        return 21
    elif a == 'V':
        return 22
    elif a == 'W':
        return 23
    elif a == 'X':
        return 24
    elif a == 'Y':
        return 25
    elif a == 'Z':
        return 26
    else:
        return 0
