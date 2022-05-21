from service import *
from agency import *


class Company:
    # initialization
    def __init__(self, name):
        self.name = name
        self.services = ServicesList()
        self.agencies = AgencyList()