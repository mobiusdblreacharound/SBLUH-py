import bloodCalc
import json
import os.path
def main(init):
    path = "./save_data.json"
    if init == True:
        if os.path.isfile(path):
            with open("save_data.json", "r") as sf:
                savefile = json.load(sf)
                print "Welcome, " + savefile["handle"] + "."
        else:
            unsaved_data = {}
            with open("save_data.json", "w") as f:
                print "========= SBLUH FIRST TIME SETUP ========="
            print "Please enter your handle in the form of:"
            print "firstwordSecondword"
            unsaved_data["handle"] = raw_input("==> ")
            # This is where I'd put my Classpect code.
            # IF I HAD ANY.
            unsaved_data["bloodColor"] = bloodCalc.main(True)
            print "[log] " + str(unsaved_data)
            with open("save_data.json", "w") as saver:
                json.dump(unsaved_data, saver)
            print "Saving Complete."
    else:
        with open("save_data.json", "r+") as sf:
            old_data = json.load(sf)
            sf.truncate()
        unsaved_data = {}
        print "playerData Reset"
        print
        print "Enter your handle. (E.X. chumHandle)"
        unsaved_data["handle"] = raw_input("==> ")
        # I seriously should make that Classpect command.
        unsaved_data["bloodColor"] = bloodCalc.main(True)
        with open("save_data.json", "r+") as newfile:
            json.dump(unsaved_data, newfile)
            print "Complete."
