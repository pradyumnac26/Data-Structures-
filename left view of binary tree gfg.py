def leftViewUtil(node,level):
    global max_level
    if (node == None): 
        return
        
    if (max_level < level):
        print(node.data,end=" ")
        max_level = level
        
    leftViewUtil(node.left, level+1);
    leftViewUtil(node.right, level+1);
def LeftView(root):
    global max_level
    max_level = 0
    leftViewUtil(root,1);
