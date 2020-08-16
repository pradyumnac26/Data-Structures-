def height(root):
    # code here
    if root is None:
        return 0
    lef=height(root.left)
    rit=height(root.right)
    return max(lef,rit)+1
