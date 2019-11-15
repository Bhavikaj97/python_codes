class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    def count(self):
        count = 0
        temp = self.head
        while (temp is not None):
            count += 1
            temp = temp.next
        return int(count)

    def last_third(self):
        n = a-3
        if n < 0:
            print("insufficient elements")
        else:
            temp = self.head
            while n > 0:
                temp = temp.next
                n -= 1
            print(temp.data)

llist = LinkedList()
llist.insert(3)
llist.insert('a')
llist.insert('a')
llist.insert(5)
llist.insert(9)
llist.insert(6)
a = llist.count()
llist.last_third()




