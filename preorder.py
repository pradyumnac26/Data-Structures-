def preOrder(root):
    if root  :
        print(root,end=" ")
        preOrder(root.left)
        preOrder(root.right)
