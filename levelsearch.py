class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def levelorder(root):
    h = height(root)
    for i in range(0, h):
        givenlevel(root, i)

def givenlevel(root, level):
    if root is None:
        return
    if level == 0:
        print("%d" %(root.data))
    elif level > 0:
        givenlevel(root.left, level-1)
        givenlevel(root.right, level-1)

def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)
    if lheight > rheight:
        return lheight+1
    else:
        return rheight+1

root = node(6)
root.left = node(3)
root.right = node(2)
root.left.left = node(1)
root.left.right = node(5)
root.left.left.left = node(8)
root.left.right.right = node(9)

print("level order traversal-")
levelorder(root)



