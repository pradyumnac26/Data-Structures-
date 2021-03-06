def findMid(head):
    counter = 0
    c1 = head

    while c1 is not None:
        c1 = c1.next
        counter += 1

    c1 = head
    for i in range(int(counter/2)):
        c1 = c1.next

    return c1.data

///////////

def findMid(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data
