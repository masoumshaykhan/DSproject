from service import *
from agency import *
from company import *
from order import *
import globals

globals.company = Company("A")


class Menu:
    # situation = "top"
    @staticmethod
    def registered_order(service, agency):
        # name = service.name
        priority = input("please enter your priority:")
        order = Order(service, priority)
        agency.orders.insert(order)
        print("your order registered :D")
        agency.orders.traverse()

    @staticmethod
    def customer_menu(situation):
        print("select service you wanna order:")
        # print services that this company support
        temp = globals.company.services.head
        while temp:
            temp.traverse(all=False)
            key = input("need it?enter number, no?enter x")
            if key == "x":
                temp = temp.next
                continue

            temp.find_id(int(key.strip()))
            service = globals.selected_service_for_find_id
            print("globals.selected_service_for_find_id", service)
            # print("srvs:", service.sid, service.name)
            temp2 = globals.company.agencies.head
            is_found = False
            # show which agencies support this service
            while temp2:
                # print("ooo", temp2.offers)
                for i in temp2.offers:
                    # print("ttt", i, key, type(i), type(key))
                    if i == int(key):
                        # print("FOUND++++++", temp2)
                        print(temp2.aid, ":", temp2.name)
                        is_found = True
                temp2 = temp2.next

            if is_found is False:
                print("this service doesnt support whit any agency")
            else:
                selected_agency_id = input("select a agency and enter its number:")
                globals.selected_agency = globals.company.agencies.find(int(selected_agency_id.strip()))
                agnc = globals.selected_agency
                # print(agnc)
                srvc = service
                print("service", srvc)
                Menu.registered_order(srvc, agnc)
                x = int(input("do yo want exit?enter 0"))
                if x == 0:
                    situation = "CUSTOMER"
                    return
                break
            print(globals.selected_agency)

            temp = temp.next
            if temp is None:
                print("this company services are finished.")
                situation = "CUSTOMER"
                return

    @staticmethod
    def menu():
        situation = "top"
        while True:
            if situation == "top":
                print("1-MANAGER")
                print("2-CUSTOMER")
                print("0-exit")
                key = int(input("pleas enter number:"))
                if key == 1:
                    situation = "MANAGER"
                elif key == 2:
                    situation = "CUSTOMER"
                elif key == 0:
                    exit(0)
            # ****MANAGER MENU****
            elif situation == "MANAGER":
                print("1-SERVICES")
                print("2-AGENCIES")
                print("0-back")
                key = int(input("pleas enter number:"))
                if key == 1:
                    situation = "SERVICES"
                elif key == 2:
                    situation = "AGENCIES"
                elif key == 0:
                    situation = "top"
            elif situation == "SERVICES":
                print("1-ADD")
                print("2-DELETE")
                print("3-PRINT")
                print("0-back")
                key = int(input("pleas enter number:"))
                if key == 1:
                    situation = "ADD"
                elif key == 2:
                    temp = globals.company.services.head
                    delete = True
                    while temp:
                        temp.traverse(all=False)
                        print("enter each services` code that you want delete and enter x for exit")
                        ss = input("enter id:")
                        if ss == "x":
                            temp = temp.next
                            continue

                        service_id_to_delete = int(ss)
                        temp2 = globals.company.agencies.head
                        while temp2:
                            for i in temp2.offers:
                                if i == 0:
                                    break
                                if service_id_to_delete == i:
                                    print(i)
                                    print("find in agencies")
                                    delete = False
                            temp2 = temp2.next
                        if delete:
                            print("tree:")
                            temp.traverse()
                            print("service_id_to_delete", service_id_to_delete)
                            temp.find_id(int(service_id_to_delete))
                            to_delete = globals.selected_service_for_find_id
                            print(" TO DELETE :", to_delete)
                            if to_delete is not None and to_delete.parent is None:
                                globals.company.services.delete_main_service(to_delete.name)
                            if to_delete is not None and to_delete.parent is not None:
                                for i in range(to_delete.parent.position + 1):
                                    # delete this service as a child of its parent
                                    if to_delete.parent.children[i].name == to_delete.name:
                                        # delete it
                                        print(to_delete.parent.children[i])
                                        del to_delete.parent.children[i]
                                        to_delete.parent.position -= 1
                                        break
                            if to_delete is not None and to_delete.parent is None:
                                del to_delete
                                break
                        else:
                            print("your agencies represent it")
                        temp = temp.next
                elif key == 3:
                    globals.company.services.traverse_lists()
                    # globals.company.services.traverse_lists(all=False)
                elif key == 0:
                    situation = "MANAGER"
            elif situation == "ADD":
                print("1-MAIN SERVICE ")
                print("2-SUB SERVICE")
                print("0-back")
                key = int(input("pleas enter number:"))
                if key == 1:
                    idd = int(input("enter service id:"))
                    name = input("enter service name:")
                    model = input("enter service model:")
                    customer_description = input("enter customer_description")
                    technical_description = input("enter technical_description")
                    expense = input("enter expense")
                    service = Service(idd, name, model, customer_description, technical_description, expense)
                    t = ServicesTree(service)
                    print(service)
                    globals.company.services.add_service_last(t)
                elif key == 2:
                    print("select service:")
                    temp = globals.company.services.head
                    counter = 1
                    while temp:
                        print(counter, ":", temp.root.name)
                        counter += 1
                        temp = temp.next
                    key = int(input("enter number:"))
                    index = key
                    temp = globals.company.services.head
                    selected = None
                    while index:
                        selected = temp
                        index -= 1
                        temp = temp.next
                    selected.traverse()
                    parent = input("enter parent service name:")
                    selected.find(parent.strip())
                    parent_service = globals.selected_service_for_find_name
                    print("subservice parent:", parent_service)
                    print("pleas create your service that you wanna add")
                    idd = int(input("enter service id:"))
                    name = input("enter service name:")
                    model = input("enter service model:")
                    customer_description = input("enter customer_description")
                    technical_description = input("enter technical_description")
                    expense = input("enter expense")
                    sub_service = Service(idd, name, model, customer_description, technical_description, expense)
                    selected.add_sub_service(parent_service, sub_service)
                    # sub_service.parent = parent_service
                    # if parent_service is not None:
                    #     parent_service.add_child(sub_service)
                elif key == 0:
                    situation = "SERVICES"
            elif situation == "AGENCIES":
                print("1-ADD AGENCIES")
                print("2-SELECT AGENCIES")
                print("0-back ")
                key = int(input("pleas enter number: "))
                if key == 1:
                    aid = input("pleas enter id of agency you wanna register:")
                    name = input("please enter name of agency you wanna register:")
                    agency = Agency(aid, name)
                    globals.company.agencies.insert_agency_last(agency)
                    print("successfully registered")
                elif key == 2:
                    print("select each agencies you wanna set its properties:")
                    globals.company.agencies.traverse_agency_list(False)
                    key = int(input("enter number:"))
                    globals.selected_agency = globals.company.agencies.find(key)
                    situation = "SELECTED AGENCY MENU"
                elif key == 0:
                    situation = "MANAGER"
            elif situation == "SELECTED AGENCY MENU":
                print()
                print("what do you want to do?")
                print("1:add offer")
                print("2:remove offer")
                print("3:PRINT ORDERS")
                print("4:DO ORDERS")
                print("0:back")

                x = int(input("enter its number:").strip())
                if x == 1:
                    if globals.selected_agency is not None:
                        globals.selected_agency.add_offer()
                        # globals.company.select_agency()
                        # TODO UNKNOWN ERROR / WE SHOULD CHECK IT OUT IF WE NEED TOP LINE COMMAND OR NOT

                if x == 2:
                    globals.selected_agency.delete_offer()
                if x == 3:
                    globals.selected_agency.orders.traverse()
                if x == 4:
                    poped = globals.selected_agency.orders.pop()
                    # print("poped:", poped)
                    globals.selected_agency.completed.push(poped)
                    print(poped)
                elif x == 0:
                    print("this order finished")
                    situation = "AGENCIES"
                else:
                    print("invalid")
            # ****CUSTOMER MENU****
            elif situation == "CUSTOMER":
                print("WELCOME")
                print("1-See this company services")
                print("0-back")
                key = int(input("input :"))
                if key == 1:
                    Menu.customer_menu(situation)
                elif key == 0:
                    situation = "top"


if __name__ == "__main__":
    s = ServicesList()

    root = Service(1, "a", "model_a", "customer_description1", "technical_description1", "expense1")
    child2 = Service(11, "b", "model_b", "customer_description_2", "technical_description_2", "expense_2")
    child2.parent = root
    root.add_child(child2)
    child4 = Service(111, "b1", "model_b1", "customer_description4", "technical_description4", "expense4")
    child4.parent = child2
    child2.add_child(child4)
    child3 = Service(112, "b2", "model_b2", "customer_description3", "technical_description3", "expense3")
    child3.parent = child2
    child2.add_child(child3)
    child1 = Service(12, "c", "model_c", "customer_description1", "technical_description1", "expense1")
    child1.parent = root
    root.add_child(child1)
    child5 = Service(113, "b3", "model_b3", "customer_description5", "technical_description5", "expense5")
    child5.parent = child2
    child2.add_child(child5)
    child6 = Service(121, "c1", "model_c1", "customer_description5", "technical_description5", "expense5")
    child6.parent = child1
    child1.add_child(child6)

    t = ServicesTree(root)
    # t.delete("b")
    # t.traverse(False)
    # exit(0)

    new_service = Service(9, "p", "model_p", "customer_description5", "technical_description5", "expense5")
    t.add_sub_service("a", new_service)
    # t.traverse()
    s.add_service_last(t)
    # print("\n ****\n")
    roott = Service(2, "aa", "model_aa", "customer_description", "technical_description", "expense")
    childd2 = Service(21, "bb", "model_bb", "customer_description2", "technical_description2", "expense2")
    childd2.parent = roott
    roott.add_child(childd2)
    childd4 = Service(211, "bb1", "model_bb1", "customer_description4", "technical_description4", "expense4")
    childd4.parent = childd2
    childd2.add_child(childd4)
    childd3 = Service(212, "bb2", "model_bb2", "customer_description3", "technical_description3", "expense3")
    childd3.parent = childd2
    childd2.add_child(childd3)
    childd1 = Service(22, "cc", "model_cc", "customer_description1", "technical_description1", "expense1")
    childd1.parent = roott
    roott.add_child(childd1)
    childd5 = Service(213, "bb3", "model_bb3", "customer_description5", "technical_description5", "expense5")
    childd5.parent = childd2
    childd2.add_child(childd5)
    childd6 = Service(221, "cc1", "model_cc1", "customer_description5", "technical_description5", "expense5")
    childd6.parent = childd1
    childd1.add_child(childd6)

    s.add_service_last(ServicesTree(roott))
    #
    # print("#############################")
    # s.traverse_lists(all=False)
    # print("#############################")

    globals.company.services = s
    a = AgencyList()
    agency1 = Agency(1, "a")
    agency1.offers[0] = 12
    # agency1.add_offer(12)
    agency1.offers[1] = 2
    # agency1.add_offer(2)
    agency1.offers[2] = 21
    # agency1.add_offer(21)
    # agency1.offers[3] =121
    agency1.pos = 3
    order = Order(roott, "needful")
    agency1.orders.insert(order)
    order = Order(child1, "essential")
    agency1.orders.insert(order)

    a.insert_agency_last(agency1)
    agency2 = Agency(2, "b")
    a.insert_agency_last(agency2)
    agency3 = Agency(3, "c")
    a.insert_agency_last(agency3)
    # a.traverse_agency_list()

    # print("###############")
    # oq = OrderQueue(100)
    # print(
    #     oq.nums
    # )
    # o1 = Order("g", "essential")
    # oq.insert(o1)
    # o2 = Order("f", "needful")
    # oq.insert(o2)
    # o3 = Order("i", "essential")
    # oq.insert(o3)
    # globals.selected_agency= agency1

    globals.company.agencies = a

    m = Menu()
    m.menu()
