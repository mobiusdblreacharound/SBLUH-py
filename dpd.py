import json
def main():
    with open("save_data.json", "r") as sdf:
        saved = json.load(sdf)
        print "You're running v1.0.0"
        print "Your Chumhandle is " + saved["handle"] + "."
        print "Your blood color is " + saved["bloodColor"] + "."
        print "Your title is " + saved["classpect"]["class"] + " of " + saved["classpect"]["aspect"] + "."
