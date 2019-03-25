class Vlan:
    """
    Implements a VLAN with VLAN number and Description.
    """

    def __init__(self, description, number):
        self.description = description
        self.number = number

    def getDescription(self):
        return self.description

    def getNumber(self):
        return self.number