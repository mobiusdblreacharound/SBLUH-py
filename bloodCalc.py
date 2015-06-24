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
