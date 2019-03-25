from Vlan import Vlan
from Port import Port

class Switch:
    """
    Implements a managable Switch with a name, list of Ports and list of implemented VLANs
    """
    def __init__(self, hostname):
        self.hostname = hostname
        self.vlans = []
        self.ports = []

    def addPortToPorts(self, consoleOutput):
        processingList = consoleOutput.rstrip("\n").split("\n")
        processingList = processingList[5:]
        for i in processingList:
            port = i.split()
            self.ports.append(Port(port[0], port[2]))

    def addVlanList(self, consoleOutput):
        processingList = consoleOutput.rstrip("\n").split("\n")
        processingList = processingList[3:]
        for i in processingList:
            vlan = i.split()
            self.vlans.append(Vlan(vlan[1], vlan[0]))

    def getPorts(self):
        return self.ports

    def getHostname(self):
        return self.hostname

    def getVlans(self):
        return self.vlans