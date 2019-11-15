class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def countnode(node):
    count = 0
    if node is None:
        return 0
    elif node.left is not None and node.right is not None:
        count = 1 + countnode(node.left) + countnode(node.right)
    else:
        count = count + countnode(node.left)
        count = count + countnode(node.right)
    return count


root = node(1)
root.left = node(3)
root.right = node(1)
root.left.left= node(4)
root.left.right = node(5)
root.left.left.left= node(9)
root.left.left.right = node(8)
root.left.left.left.left= node(9)
print(countnode(root))

