def deleteNode(head, position):
    if position==0:
        head=head.next
    prev=head
    curr=head
    for i in range(position):
        prev=curr
        if curr==None:
            break
        else :
            curr=curr.next
    prev.next=curr.next
    return head
