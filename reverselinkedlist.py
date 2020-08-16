def reverseList(head):
    if head is None:
        return None
    
    prev = None
    curr = head

    
    while curr is not None:
        next = curr.next       # Take the next node as ahead
        curr.next = prev        # Link current node to its previous
        prev = curr             # update prev as the current node
        curr = next            # update curr
    
    return prev
   
