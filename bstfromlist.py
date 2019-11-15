class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


def insert(self,d):
    if self.data == d:
        return
    elif d < self.data:
        if self.left:
            return insert(self.left,d)
        else:
            self.left = Node(d)
    else:
        if self.right:
            return insert(self.right,d)
        else:
            self.right = Node(d)


lst = [12, 7, 16, 5, 8, 14 ]
root = None
if lst is not None:
    root = Node(lst[0])
    for i in range(1, len(lst)):
        insert(root,lst[i])

print()

