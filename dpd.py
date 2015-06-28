import json
def main():
    with open("save_data.json", "r") as sdf:
        saved = json.load(sdf)
        print "You're running v0.1.1a2"
        print "Your Chumhandle is " + saved["handle"] + "."
        print "Your blood color is " + saved["bloodColor"] + "."
        # print "Your title is " + saved["classpect"] + "."
