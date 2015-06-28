def main(isInit):
    firstName = raw_input("Enter First Name: ")
    firstNameUpper = firstName.upper()
    print
    lastName = raw_input("Enter Last Name: ")
    lastNameUpper = lastName.upper()

    firstNameConverted = calc(firstName)
    lastNameConverted = calc(lastName)
    print str(firstNameConverted) + ' + ' + str(lastNameConverted)

def calc(input):
    data = input
    data = data.upper()
    inputUpper = data
    beginConvert = [ inputUpper[0] ]
    endConvert = list(inputUpper)
    finalStuff = listAspect(beginConvert) + listAspect(endConvert)

    return finalStuff

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
