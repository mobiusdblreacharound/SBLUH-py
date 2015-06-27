import json
import bloodCalc
import sweepCalc

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
        elif stuff == "help:bloodCalc":
            print "information"
        elif stuff == "help:sweepCalc":
            print "information"
        elif stuff == "help:playerData":
            print "information"
        elif stuff == "help:displayPlayerData":
            print "information"
        elif stuff == "aspect":
            unfin() # Still gotta do this sometime, prioritizing help commands
        elif stuff == "bloodCalc":
            bloodCalc.main(False)
        elif stuff == "sweepCalc":
            sweepCalc.calc()
        elif stuff == "playerData":
            unfin()
        elif stuff == "displayPlayerData":
            unfin()
        else:
            print "'" + stuff + "' is not a valid command. Use \"help\" for information."

console()
