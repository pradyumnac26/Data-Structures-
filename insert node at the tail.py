def insertNodeAtTail(head, data):
    node = SinglyLinkedListNode(data)
    
    if head:
        current = head
        while current.next:
            current = current.next
        current.next = node
    else:
        head = node
    return head
    
