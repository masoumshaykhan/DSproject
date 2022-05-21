import globals
from order import *
from service import *


# import menu
# import array


class Agency:
    # initialization
    completed = CompletedOrders()
    services = ServicesList()
    orders = OrderQueue(1000)
    offers = None  # services that this agency support
    pos = 0

    def __init__(self, aid, name):
        """

        :param aid:
        :param name:
        """
        self.name = name
        self.aid = aid  # aid means agency`s iD
        self.next = None
        self.offers = [0] * 100

    # to string method
    def __str__(self):
        return "Name:{} Services:{}".format(self.name, self.services.traverse_lists())

    # set agencies services
    def add_offer(self):
        """
        :return:
        """
        temp = globals.company.services.head
        while temp:
            temp.traverse(all=False)
            print("enter each services` code and enter x for exit")

            while True:
                ss = input("enter id:")
                if ss == "x":
                    break
                self.offers[self.pos] = int(ss)
                self.pos += 1
            temp = temp.next
        # globals.company.select_agency()
        # TODO UNKNOWN ERROR / WE SHOULD CHECK IT OUT IF WE NEED TOP LINE COMMAND OR NOT

    # remove service from agency
    def delete_offer(self):
        temp = globals.company.services.head
        while temp:
            # show services to a manager
            temp.traverse(all=False, offers=self.offers)
            print("enter each services` code you wanna delete and enter x for exit")
            i = 0
            while True:
                ss = input("enter id:")
                if ss == "x":
                    break

                for i in range(0, self.pos + 1):
                    # print(ss, i, self.pos, self.offers[i])
                    if int(ss) == self.offers[i]:
                        del self.offers[i]
                        self.pos -= 1

            temp = temp.next

        # TODO Go To Top Level Of Menu

    def add_order(self, order):
        pass

    def show_orders(self):
        pass

    # def copy(self):
    #     new_agency = Agency(self.aid,self.name)
    #     new_agency.offers = self.offers.copy();


# save agencies in a linked list
class AgencyList:
    # initialization
    head = None

    def __init__(self):
        self.head = None

    # Adding object to linked list :
    # At the last:
    def insert_agency_last(self, new_data):
        new_node = new_data
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        return temp.next

    # get id of service then look for it and return
    def find(self, idd):
        temp = self.head
        while temp:
            if temp.aid == idd:
                return temp
            temp = temp.next

    """See our linked List objects in 2 way
    1:print object with to string method
    2: just print objects name"""

    def traverse_agency_list(self, all=True):
        temp = self.head
        counter = 1
        while temp:
            if all:
                print(temp)
            else:
                globals.agencies_temp_name_index += str(counter) + " " + temp.name + "\n"
                temp.aid = counter
                print(temp.aid, ":", temp.name)
                counter += 1
            temp = temp.next
