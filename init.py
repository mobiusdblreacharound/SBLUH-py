import bloodCalc
import os.path
import json
def main(init):
    path = "./save_data.json"
    if init == True:
        if os.path.isfile(path):
        else:
            unsaved_data = {}
            with open("save_data.json", "w"):
                print "========= SBLUH FIRST TIME SETUP ========="
            print "Please enter your handle in the form of:"
            print "firstwordSecondword"
            unsaved_data["handle"] = raw_input("==> ")
            # This is where I'd put my Classpect code.
            # IF I HAD ANY.
            unsaved_data["bloodColor"] = bloodCalc(True)
            print "[ignore] " + unsaved_data
            with open("save_data.json", "w") as saver:
                json.dump(unsaved_data, saver)
            print "Saving Complete."
    else:
