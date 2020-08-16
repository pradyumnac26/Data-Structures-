def levelOrder(root):
    q=[]
    if root is None :
        return
    q.append(root)
    while len(q)>0:
        print( q[0].info,end=' ')
        nd=q.pop(0)
        if nd.left is not None:
            q.append(nd.left)
        if nd.right is not None:
            q.append(nd.right)
