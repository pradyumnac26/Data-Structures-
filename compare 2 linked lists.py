def compare_lists(llist1, llist2):
    if not llist1 and not llist2:
        return 1
    elif (llist1 and llist2) and (llist1.data==llist2.data):
        return compare_lists(llist1.next,llist2.next)
        
    else :
        return 0
