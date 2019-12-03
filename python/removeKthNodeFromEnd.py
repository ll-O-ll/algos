def removeKthNodeFromEnd(head, k):
    first = head
    second = head
    idx = 1
    while idx <= k:
        second = second.next
        idx += 1:
    if second is None: #remove last element
        head.value = head.next.value
        head.next = head.next.next
        return
    while second.next is not None:
        second = second.next
        first = first.next 
    first.next = first.next.next
    return