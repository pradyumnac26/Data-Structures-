def has_cycle(head):
    curr=head
    lst=list()
    while curr!=None:
        if curr in lst:
            return 1
        lst.append(curr)
        curr=curr.next
    return 0
