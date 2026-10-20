class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end = " ")
        inorder(root.right)

def insert(root,key):
    if not root:
        return Node(key)

    if root.data > key:
        root.left = insert(root.left,key)

    else:
        root.right = insert(root.right,key)

    return root

def minValueNode(root):
    c = root
    while c.left is not None:
        c = c.left
    return c

def delete(root,key):
    if root is None:
        return root

    if root.data > key:
        root.left = delete(root.left,key)

    elif root.data < key:
        root.right = delete(root.right,key)

    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minValueNode(root.right)
        root.data = temp.data
        root.right = delete(root.right,temp.data)
    return root

root = None
root = insert(root,50)
root = insert(root,70)
root = insert(root,30)
root = insert(root,20)
root = insert(root,80)
root = insert(root,40)
root = insert(root,60)

print("In-order Traversal of Original Tree")
inorder(root)

print()

print("\nDelete 20")
root = delete(root,20)
print("In-order traversal after deleting 20")
inorder(root)

print()

print("\nDelete 30")
root = delete(root,30)
print("In-order traversal after deleting 30")
inorder(root)

print()

print("\nDelete 50")
root = delete(root,50)
print("In-order traversal after deleting 50")
inorder(root)
