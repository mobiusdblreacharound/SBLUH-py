def test():
    print "bloodCalc OK!"

def calculate(sign):
    data = sign.upper()

    x = 0

    if data == "ARIES":
        x = x + 1
        return x
    elif data == "TAURUS":
        x = x + 2
        return x
    elif data == "GEMINI":
        x = x + 3
        return x
    elif data == "CANCER":
        x = x + 4
        return x
    elif data == "LEO":
        x = x + 5
        return x
    elif data == "VIRGO":
        x = x + 6
        return x
    elif data == "LIBRA":
        x = x + 7
        return x
    elif data == "SCORPIO":
        x = x + 8
        return x
    elif data == "SAGITTARIUS":
        x = x + 9
    elif data == "CAPRICORN":
        x = x + 10
    elif data == "AQUARIUS":
        x = x + 11
    elif data == "PISCES":
        x = x + 12
    else:
        return 4

def find(sign1, sign2):

    data = bloodCalc.calculate(sign1) + bloodCalc.calculate(sign2)

    if data == 2 or data == 3:
        return "Burgundy"
    elif data == 4 or data == 5:
        return "Brown"
    elif data == 6 or data == 7:
        return "Yellow"
    elif data == 8:
        return "Mutant/Candy Red"
    elif data == 9:
        return "Lime"
    elif data == 10 or data == 11 or data == 13:
        return "Green"
    elif data == 12:
        return "Jade"
    elif data == 14 or data == 15:
        return "Teal"
    elif data == 16 or data == 17:
        return "Cerulean"
    elif data == 18 or data == 19:
        return "Indigo"
    elif data == 20 or data == 21:
        return "Purple"
    elif data == 22 or data == 23:
        return "Violet"
    elif data == 24:
        return "Fuchsia"
