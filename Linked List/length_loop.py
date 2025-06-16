# Given the head of a linked list. The task is to find the length of the loop in the linked list.
# If the loop is not present return 0.

# Examples:

# Input: head: 1  → 2  → 3  → 4  → 5  → 2
# Output: 4
# Explanation: There exists a loop in the linked list and the length of the loop is 4. 

class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None

head = LinkedList(1)
head.next = LinkedList(2)
head.next.next = LinkedList(3)
head.next.next.next = LinkedList(4)
head.next.next.next.next = LinkedList(5)
head.next.next.next.next.next = head.next

def show_linked_list(head:LinkedList):
    current = head
    output = ""

    while current:
        output = output + f'{current.data}->'
        current = current.next
    
    output = output + "->NULL"
    return output

# print(show_linked_list(head))

def length_loop(head:LinkedList):
    slow = head
    fast = head.next
    n = 0

    while fast.next.next:
        if slow == fast:
            length = 1
            place = slow.next

            while place != fast:
                length = length + 1
                place = place.next

            return length
        
        slow = slow.next
        fast = fast.next.next
        n = n + 1

    
    return 0

print(length_loop(head))


