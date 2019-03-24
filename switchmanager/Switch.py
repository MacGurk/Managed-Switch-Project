class Switch:
    """
    Implements a managable Switch with a name, list of Ports and list of implemented VLANs
    """
    def __init__(self, name):
        self.name = name
        self.vlans = []
        self.ports = []

    def addPortToPorts(self, port):
        self.ports.append(port)



    def getPorts(self):
        return self.ports

    def getName(self):
        return self.name

    def getVlans(self):
        return self.vlans