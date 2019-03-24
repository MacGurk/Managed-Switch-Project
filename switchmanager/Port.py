class Port:
    def __init__(self, portNr, portVlan):
        self.portNr = portNr
        self.portVlan = portVlan

    def getPortNr(self):
        return self.portNr

    def getPortVlan(self):
        return self.portVlan