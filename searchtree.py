class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def bst(root, num):
    if root is None:
        return False
    elif root.data == num:
        return True
    elif num < root.data:
        return bst(root.left, num)
    elif num > root.data:
        return bst(root.right, num)


root = node(10)
root.left = node(8)
root.right = node(15)
root. right.left = node(12)
root.right.right = node(20)


num = 9
result = bst(root, num)
print(result)

