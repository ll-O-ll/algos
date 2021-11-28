import math
# Add any extra import statements you may need here


class Node:
  def __init__(self, x):
    self.data = x
    self.next = None

# Add any helper functions you may need here

"""
O(n) solution on lc discussions:

def reverse(head):

  # Reverses a sublist of the linked list (`start` node is inclusive, while `end`node is exclusive).
  def reverseSublist(start, end):
    prev = end # set the prev to end to link up the newly reversed tail to the next node
    curr = start
    
    while curr != end:
      next = curr.next
      curr.next = prev
      prev = curr
      curr = next
      
    return prev
  
  dummy = Node(0)
  dummy.next = head
  prev = dummy
  curr = head

  while curr:
    start = curr
    
    while curr and curr.data % 2 == 0: # Keep advancing the fast pointer until it reaches an odd-valued node or the end of the list.
      curr = curr.next
      
    if start != curr: # Signifies that there is a list to reverse.
      prev.next = reverseSublist(start, curr)

    if curr:
      prev = curr
      curr = curr.next
    
  return dummy.next

"""

def reverse_sub_part(head, first_node, last_node):
    prev_node = None
    curr_node = head
    # find first node in linked list to start reverse op
    while curr_node is not first_node:
        prev_node = curr_node
        curr_node = curr_node.next
    # reverse op
    tmp_prev = prev_node 
    while curr_node != last_node:
        tmp_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = tmp_node
    if tmp_prev != None:
        tmp_prev.next = prev_node
    first_node.next = last_node
    return prev_node
        
def reverse(head):
   
    '''
    three cases: 1 - subpart starts at idx 0
                 2 - bordered by odd numbers which is covered here:
                 3 - subpart appended to list (end of list)
    '''

    curr_node = head
    prev_node = None
    len_sub_part = 0

    # case 1:
    if head.data % 2 == 0:
        first_node = head
        while curr_node.data % 2 == 0:
            curr_node = curr_node.next
        head = reverse_sub_part(head, first_node, curr_node)

    while curr_node != None:
        # case 2 covered in loop
        if curr_node.data % 2 == 0: # if the node's data is even
            if len_sub_part == 0:
                # store first node of linked list in var for reverse operation
                first_node = curr_node
            len_sub_part += 1
            
        else: # the node's data is odd
            if len_sub_part > 0: # this means the odd numbers borders the right side of the subpart -> means end of subpart which we can proceed to reverse
                reverse_sub_part(head, first_node, curr_node)
            len_sub_part = 0

        prev_node = curr_node
        curr_node = curr_node.next
    
    # case 3:
    if len_sub_part > 0:
        reverse_sub_part(head, first_node, curr_node) 

    return head

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printLinkedList(head):
    print('[', end='')
    while head != None:
        print(head.data, end='')
        head = head.next
        if head != None:
            print(' ', end='')
    print(']', end='')

test_case_number = 1

def check(expectedHead, outputHead):
    global test_case_number
    tempExpectedHead = expectedHead
    tempOutputHead = outputHead
    result = True
    while expectedHead != None and outputHead != None:
        result &= (expectedHead.data == outputHead.data)
        expectedHead = expectedHead.next
        outputHead = outputHead.next

    if not(outputHead == None and expectedHead == None):
        result = False

    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, ' Test #', test_case_number, sep='')
    else:
        print(wrongTick, ' Test #', test_case_number, ': Expected ', sep='', end='')
        printLinkedList(tempExpectedHead)
        print(' Your output: ', end='')
        printLinkedList(tempOutputHead)
        print()
    test_case_number += 1

def createLinkedList(arr):
    head = None
    tempHead = head
    for v in arr:
        if head == None:
            head = Node(v)
            tempHead = head
        else:
            head.next = Node(v)
            head = head.next
    return tempHead

if __name__ == "__main__":

    head_1 = createLinkedList([1, 2, 8, 9, 12, 16])
    expected_1 = createLinkedList([1, 8, 2, 9, 16, 12])
    output_1 = reverse(head_1)
    check(expected_1, output_1)

    head_2 = createLinkedList([2, 18, 24, 3, 5, 7, 9, 6, 12])
    expected_2 = createLinkedList([24, 18, 2, 3, 5, 7, 9, 12, 6])
    output_2 = reverse(head_2)
    check(expected_2, output_2)
    
    head_3 = createLinkedList([2, 8, 9, 11, 12, 16])
    expected_3 = createLinkedList([8, 2, 9, 11, 16, 12])
    output_3 = reverse(head_3)
    check(expected_3, output_3)

  # Add your own test cases here
  