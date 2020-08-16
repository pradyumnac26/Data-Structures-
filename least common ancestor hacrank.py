
def lca(root, v1, v2):
    while root:
        if root.info>v1 and root.info>v2:
            root=root.left
        elif root.info<v1 and root.info<v2:
            root=root.right
        else :
            break
    return root
