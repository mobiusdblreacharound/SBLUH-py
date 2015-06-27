import json
import bloodCalc
import sweepCalc

print "SBLUH CONSOLE"
print "Python Edition"
print
init.main(True)
print "run 'help' for commands."

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
            print "Displays your blood color as if you were a troll."
        elif stuff == "help:sweepCalc":
            print "Converts Years to Alternian Sweeps and vice versa."
        elif stuff == "help:playerData":
            print "So far it does nothing."
        elif stuff == "help:displayPlayerData":
            print "It doesn't exist yet."
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
