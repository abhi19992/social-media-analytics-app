class KeyFetcher:

    def __init__(self):
        pass
    def getKeys(self, keysFileName):
        f = open(keysFileName, "r")
        keys = f.read()

        clientKey = keys[:keys.index('\n')]
        clientSecret = keys[(keys.index('\n')+1):]

        return clientKey, clientSecret


## Driver code
kf = KeyFetcher()
clientKey, clientSecret = kf.getKeys("api_keys.txt")
print(clientKey)
print(clientSecret)