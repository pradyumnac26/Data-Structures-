def LCA(root, n1, n2):
    if root is None:
        return None
    while root!=None:
        if root.data>n1 and root.data>n2:
            root=root.left
        elif root.data<n1 and root.data<n2:
            root=root.right
        else :
            return root
            break
