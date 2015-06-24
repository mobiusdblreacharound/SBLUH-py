import json
import bloodCalc

print "SBLUH CONSOLE"
print "Python Edition"

def unfin():
    print "I need to code this!"
    print "github.com/Nutzchannel/SBLUH-py/issues"

def console():
    while True:
        enterSpam = 0
        stuff = raw_input("==> ")
        if stuff == "help":
            print "Available commands: help, aspect, bloodCalc, sweepCalc, playerData, and displayPlayerData"
            print "Enter help:<command> for information on \"command\"."
        elif stuff == "help:aspect":
            print "[u] Displays your Classpect (Class and Aspect)."
            console()
        elif stuff == "aspect":
            unfin()
        elif stuff == "bloodCalc":
            bloodCalc.main(False)
        elif stuff == "sweepCalc":
            unfin()
        elif stuff == "playerData":
            unfin()
        elif stuff == "displayPlayerData":
            unfin()
        else:
            print "'" + stuff + "' is not a valid command. Use \"help\" for information."

console()
