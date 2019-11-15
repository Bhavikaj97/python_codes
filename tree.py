class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def size(node):
    if node is None:
        return 0
    else:
        return (size(node.left) + size(node.right) + 1)

def Depth(node):
    if node is None:
        return 0
    else:
        d1 = Depth(node.left)
        d2 = Depth(node.right)
        if d1 >= d2:
            return d1 + 1
        elif d2 > d1:
            return d2 + 1

def leafcount(node):
    if node is None:
        return 0
    if ((node.left)is None and(node.right) is None):
        return 1
    else:
        return (leafcount(node.left) + leafcount(node.right))


root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left= node  (4)
root.left.right = node(5)

print("size of tree is", size(root))
print("depth of tree is", Depth(root))
print("no. of leaves of tree is", leafcount(root))

