def insertNodeAtPosition(head, data, position):
    x=SinglyLinkedListNode(data)
    current=head
    for i in range(position-1):
        current=current.next
    x.next=current.next
    current.next=x
    return head
