import json

def loadAPIKey():
    with open("data/key/apiKey.json") as jsonFileRead:
        apiKey = json.load(jsonFileRead)
    return apiKey["API_Key"]


def loadSecretKey():
    with open("data/key/apiKey.json") as jsonFileRead:
        secretKey = json.load(jsonFileRead)
    return secretKey["Secret_Key"]

    
def writeAPIKey(apiKey, secretKey):
    with open("data/key/apiKey.json") as jsonFileRead:
        saveKeys = json.load(jsonFileRead)
        saveKeys["API_Key"] = apiKey
        saveKeys["Secret_Key"] = secretKey
    
    with open("data/key/apiKey.json", "w") as jsonFileWrite:
            json.dump(saveKeys, jsonFileWrite)
    return
