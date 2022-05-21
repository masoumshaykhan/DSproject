import datetime

import array as arr

my_turn = 1


class Order:
    name = None
    priority = ""

    # initialization
    def __init__(self, name, priority):
        global my_turn  # increase when order registered
        self.name = name
        self.turn = my_turn
        my_turn += 1
        # use int as priorities
        if priority == "essential":
            self.priority = 3
        elif priority == "needful":
            self.priority = 2
        elif priority == "ordinary":
            self.priority = 1
        # save the exact time of registering orders
        self.time = datetime.datetime.now()
        self.next = None

    def hash_code(self):
        """
        create a hash for each order according to their priority
        :return:
        """
        n = 1000
        temp = self.priority * n
        temp2 = n - self.turn
        return temp + temp2

    def __str__(self):
        return "Name:{} Priority:{} Time:{}".format(self.name.name, self.priority, self.time)


class OrderQueue:
    # initialization
    def __init__(self, max_size):
        self.size = 0
        self.max_size = max_size
        self.nums = [None for i in range(self.max_size)]

    def max_heapify(self, n, k):
        """
        sorts orders based on order on the heap
        :param n:
        :param k:
        :return:
        """
        l = self.left(k)
        r = self.right(k)
        if l < n \
                and self.nums[l] is not None \
                and self.nums[k] is not None \
                and self.nums[l].hash_code() > self.nums[k].hash_code():
            largest = l
        else:
            largest = k
        if r < n \
                and self.nums[r] is not None \
                and self.nums[largest] is not None \
                and self.nums[r].hash_code() > self.nums[largest].hash_code():
            largest = r
        if largest != k:
            temp = self.nums[k]
            self.nums[k] = self.nums[largest]
            self.nums[largest] = temp
            self.max_heapify(n, largest)

    def left(self, k):
        """
        get us left child index
        :param k:
        :return:
        """
        return 2 * k + 1

    def right(self, k):
        """
        get us right child index
        :param k:
        :return:
        """
        return 2 * k + 2

    def build_max_heap(self, n):
        """

        :param n:
        :return:
        """
        l = int((n // 2) - 1)
        for k in range(l, -1, -1):
            self.max_heapify(n, k)

    def add(self, obj):
        """
        add new order to our heap
        :param obj:
        :return:
        """
        length = len(self.nums)
        length = length + 1
        self.nums[length - 1] = obj
        self.build_max_heap(length)

    def insert(self, obj):
        if self.size >= self.max_size:
            # if self.size >= len(self.nums):
            print("list index out of range")
            return

        self.nums[self.size] = obj
        self.size += 1
        self.build_max_heap(self.size)

    def pop(self):
        root = 0
        print(self.size, "*--*")
        to_pop = self.nums[root]
        print("to pop", to_pop)
        last = self.nums[self.size - 1]
        self.nums[root] = last
        self.size -= 1
        self.nums[self.size] = 0
        self.build_max_heap(self.size)
        print("to pop", to_pop)
        return to_pop

    def traverse(self):
        for i in range(len(self.nums) // 2):
            if self.nums[i] is not None:
                print(" PARENT : " + str(self.nums[i]))
                if len(self.nums) > self.left(i):
                    if self.nums[self.left(i)] is not None:
                        print(" LEFT CHILD : " + str(self.nums[self.left(i)]))
                if len(self.nums) > self.right(i):
                    if self.nums[self.right(i)] is not None:
                        print(" RIGHT CHILD : " + str(self.nums[self.right(i)]))


class IsEmptyError(Exception):
    pass


class CompletedOrders:
    # initialization
    def __init__(self):
        self.head = None
        self.size = 0

    # Give us length of stack
    def len(self):
        return self.size

    # tell us if stack is full or not
    def is_empty(self):
        return self.size == 0

    # add node as a last node of the stack
    def push(self, order):
        if self.head is None:
            self.head = order
        else:
            temp = order
            temp.next = self.head
            self.head = temp
        self.size += 1

    # remove last node of stack
    def pop(self):
        if self.is_empty():
            raise IsEmptyError("stack is empty")
        else:
            result = self.head.data
            self.head = self.head.next
        self.size -= 1
        return result

    # get us the top of stack
    def top(self):
        if self.is_empty():
            raise IsEmptyError("stack is empty")
        return self.head.data

    # see stack
    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

# nums = [3, 1, 4, 6, 9, 2, 5, 4]
# o = OrderQueue()
# o.nums = nums
# o.build_max_heap(len(nums))
# print(nums)
