def calc():
    print "Enter Mode."
    print "Years to Sweeps = 0"
    print "Sweeps to Years = 1"
    print
    sweep = raw_input("==> ")
    if sweep == "0":
        sweepCalc.req(sweep)
    elif sweep == "1":
        sweepCalc.req(sweep)
    else:
        print "Invalid entry."
        print
        sweepCalc.calc()

def req(stuff):
    if stuff == "0":
        tosweeps = True
        print "Enter Years."
        value = raw_input("==> ")
        print value + " years == " + sweepCalc.conv(int(value), tosweeps) + " sweeps."
    elif stuff == "1":
        tosweeps = False
        print "Enter Sweeps."
        value = raw_input("==> ")
        print value + " sweeps == " + sweepCalc.conv(int(value), tosweeps) + "years."

def conv(x, sweeps):
    y = 0.0
    if sweeps == True:
        y = x / 2.166666666666667
    elif sweeps == False:
        y = x * 2.166666666666667
    return str(y)
