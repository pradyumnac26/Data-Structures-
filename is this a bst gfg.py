def check_binary_search_tree_(root):
    INT_MIN=-1000000
    INT_MAX=10000000
    return checkBST(root, INT_MIN, INT_MAX)

def checkBST(root, Min, Max):
    if not root:
        return True
    if root.data <= Min or root.data >= Max:
        return False
    return checkBST(root.left, Min, root.data) and checkBST(root.right, root.data, Max)
