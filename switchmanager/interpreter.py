def createListOfOutputOnLinebreak(output):
    return output.rstrip("\n").split("\n")

def getDeviceName(string):
    return string.lstrip("(").rstrip(")  #")