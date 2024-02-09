import json;

def saveSettingsJson(data):
    """Saves the settings to a json file"""
    with open("config.json", "w") as f:
        json.dump(data, f);
    pass


def loadSettings():
    """Loads the settings from a json file and parses into a Settings object"""
    # Read config.json, if doesnt exist, create it
    try:
        with open("config.json", "r") as f:
            data = json.load(f);
            return data;
    except:
        with open("config.json", "w") as f:
            data = {
                "EmulatorDelay" : 1,
                "ResolutionX" : 64,
                "ResolutionY" : 32,
                "ScalingFactor" : 20,
                "Debug" : False,
                "RomName" : "pong.ch8"
            }
            json.dump(data, f);
            return data;




