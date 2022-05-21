import globals


class Service:
    # initialization
    position = -1

    def __init__(self, sid, name, model, customer_description, technical_description, expense):
        self.parent = None
        self.next = None
        self.sid = sid
        self.name = name
        self.model = model
        self.is_offer = False
        self.customer_description = customer_description
        self.technical_description = technical_description
        self.expense = expense
        self.children = [None] * 100
        # self.position = -1
        # self.parents = []

    # add child of each node of tree
    def add_child(self, obj):
        # print("pos" , self.name , self.position)
        self.position += 1
        print("pos", self.name, self.position)
        self.children[self.position] = obj

    # to string method
    def __str__(self):
        return "ID:{} Name:{} Model:{} Customer Description:{} Technical Description:{} " \
               "Children Count:{}\n \tPARENT:{}".format(
            self.sid, self.name, self.model, self.customer_description, self.technical_description, len(self.children),
            self.parent)


# make a tree for each main service
class ServicesTree:
    # initialization
    root = None

    def __init__(self, root):
        if root is not None:
            self.root = root
        self.next = None

    # searching for a specific service and find it then return
    def find(self, data):
        print(data)
        # checking specific service`s data with root of tree
        print("root :", self.root.name)
        if self.root.name == data:
            return self.root
        # checking whit other level of tree
        for k in range(self.root.position + 1):
            s = self.root.children[k]
            print("s name:", s.name)
            if s.name == data:
                return s
            else:
                # make it recursive
                self.find_helper(s.position, s.children, data)

    def find_helper(self, position, child, data):
        for k in range(position + 1):
            c = child[k]
            print("h c name :", c.name)
            if c.name == data:
                return c
            else:
                self.find_helper(c.position, c.children, data)

    def find_id(self, idd):
        print(idd)
        # checking specific service`s data with root of tree
        # print("root :", self.root.name)
        if self.root.sid == idd:
            return self.root
        # checking whit other level of tree
        for k in range(self.root.position + 1):
            s = self.root.children[k]
            # print("s id:", s.sid)
            # if s is not None:
            if s.sid == idd:
                print("s id:", s.sid)
                return s
            else:
                # make it recursive
                return self.find_id_helper(s.position, s.children, idd)

    def find_id_helper(self, position, child, idd):
        for k in range(position + 1):
            c = child[k]
            # print("h c id :", c.sid)
            if c.sid == idd:
                return c
            else:
                self.find_helper(c.position, c.children, idd)

    #
    def delete(self, data):
        """delete specific services of tree
        :param data:
        :return:
        """
        # at first find it
        to_delete = self.find(data)
        for i in range(to_delete.parent.position + 1):
            # for i in range(len(to_delete.parent.children)):
            # delete this service as a child of its parent
            if to_delete.parent.children[i].name == to_delete.name:
                # delete it
                del to_delete.parent.children[i]
                break

    def delete_service_in_company(self):
        """delete specific services of tree from hole company
        :return:
        """
        temp = globals.company.services.head
        delete = True
        while temp:
            temp.traverse(all=False)
            print("enter each services` code that you want delete and enter x for exit")
            ss = input("enter id:")
            if ss == "x":
                break
            service_id_todelete = int(ss)
            temp2 = globals.company.agencies.head
            while temp2:
                for i in temp2.offers:
                    if service_id_todelete == i:
                        delete = False
                temp2 = temp2.next
            if delete:
                to_delete = self.find_id(int(service_id_todelete))
                print(to_delete)
                for i in range(to_delete.parent.position + 1):
                    # delete this service as a child of its parent
                    if to_delete.parent.children[i].name == to_delete.name:
                        # delete it
                        print(to_delete.parent.children[i])
                        del to_delete.parent.children[i]
                        break
            temp = temp.next

    # set specific service parent as main service that you get us
    def add_sub_service(self, main_service, new_service):
        to_add = self.find(main_service)
        new_service.parent = to_add
        to_add.add_child(new_service)

    def traverse(self, all=True, offers=None):
        """print our tree in 3way
         1:print each object using to string method
         2:print just name of services
         3:print each nodes of tree that a specific agency represent
        :param all:
        :param offers:
        :return:
        """

        if offers is None:
            if all is False:
                print(self.root.sid, ":", self.root.name)
            else:
                print(self.root)

            for k in range(self.root.position + 1):
                c = self.root.children[k]
                if c is not None:
                    if all is False:
                        print(c.sid, ":", c.name)
                        self.traverse_helper(c, all=all)
                    else:
                        print(c)
                        self.traverse_helper(c, all=all)

        # offer is not None
        else:
            if all is False:
                if self.root.sid in offers:
                    print(self.root.sid, ":", self.root.name)

            else:
                if self.root.sid in offers:
                    print(self.root)

            for k in range(self.root.position + 1):
                c = self.root.children[k]
                if c is not None:
                    if all is False:
                        if c.sid in offers:
                            print(c.sid, ":", c.name)
                            self.traverse_helper(c, all=all, offers=offers)
                    else:
                        if c.sid in offers:
                            print(c)
                            self.traverse_helper(c, all=all, offers=offers)

    def traverse_helper(self, i, all=True, offers=None):
        if offers is not None:
            if i is not None:
                for k in range(i.position + 1):
                    c = i.children[k]
                    if all is False:
                        if c.sid in offers:
                            print(c.sid, ":", c.name)
                    else:
                        if i.sid in offers:
                            print(c)
                    self.traverse_helper(c, offers=offers)
        # offer is None
        else:
            if i is not None:
                for k in range(i.position + 1):
                    c = i.children[k]
                    if all is False:
                        if c is not None:
                            print(c.sid, ":", c.name)
                    else:
                        if c is not None:
                            print(c)
                    self.traverse_helper(c, offers=offers)

        # if i is not None:
        #     for k in range(i.position + 1):
        #         c = i.children[k]
        #         if all is False:
        #             if c.sid in offers:
        #                 print(c.sid, ":", c.name)
        #         else:
        #             if offers is not None and i.sid in offers:
        #                 print(c)
        #         self.traverse_helper(c, offers=offers)
    # else:
    #     pass
    # TODO Should check if we want to print services at offers situation


# save trees of services in a linked list
class ServicesList:
    # initialization
    head = None

    def __init__(self):
        self.head = None

    # Adding object to linked list :
    # At the last:
    def add_service_last(self, new_data):
        new_node = new_data
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        return temp.next

    def delete_service(self, data):
        # Store head node
        temp = self.head
        # If head node itself holds the key to be deleted
        if temp is not None:
            if temp.name == data:
                self.head = temp.next
                temp = None
                return

        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while temp is not None:
            if temp.name == data:
                break
            prev = temp
            temp = temp.next

            # if key was not present in linked list
            if temp is None:
                return

            # Unlink the node from linked list
            prev.next = temp.next
            temp = None

    # get id of agency then look for it and return
    def find(self, idd):
        temp = self.head
        service = None
        while temp:
            service = temp.find_id(idd)
            temp = temp.next
        return service

    # See our linked List objects:
    # objects are a tree
    def traverse_lists(self, all=True, offers=None):
        temp = self.head
        while temp:
            print(temp.traverse(all, offers))
            temp = temp.next
