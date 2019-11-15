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


    def remove_duplicate(self):
        hash = set()
        curr_node = self.head
        prev_node = None
        while (curr_node != None):
            if(curr_node.data in hash):
                prev_node.next = curr_node.next
                curr_node = None
            else:
                hash.add(curr_node.data)
                prev_node = curr_node
            curr_node = prev_node.next


    def printlist(self):
        temp = self.head
        while temp:
            print ((temp.data), end=" ")
            temp = temp.next


llist = LinkedList()
llist.insert(3)
llist.insert('a')
llist.insert('a')
llist.insert(6)
llist.insert(9)
llist.insert(6)
llist.remove_duplicate()
llist.printlist()

print()










def delete_node(self,key):
    temp = self.head
    if temp is not None:
        if(temp == key):
            self.head = temp.next
            temp = None
            return





