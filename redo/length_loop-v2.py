# Given the head of a linked list. The task is to find the length of the loop in the linked list.
# If the loop is not present return 0.

# Examples:

# Input: head: 1  → 2  → 3  → 4  → 5  → 2
# Output: 4
# Explanation: There exists a loop in the linked list and the length of the loop is 4. 

class LinkedList:
    def __init__(self , data):
        self.data = data
        self.next = None
        pass

head = LinkedList(1)
head.next =LinkedList(2)
head.next.next = LinkedList(3)
head.next.next.next = LinkedList(4)
head.next.next.next.next = LinkedList(5)
head.next.next.next.next.next = head.next.next

def print_linked_list(input:LinkedList):
    output = ""

    while input:
        output = output + f'{input.data}->'
        print("outtt",output)
        input = input.next

    output = output + 'null'
    return output

# print(print_linked_list(head))

def length_loop(head:LinkedList):

    slow = head
    fast = head
    loop_exists = False
    length = 0

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            loop_exists = True
            break

    if not loop_exists:
        return length
    
    temp = slow.next

    while temp != slow:
        length += 1
        temp = temp.next



    return length

print(length_loop(head))



