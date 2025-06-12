# Given a singly linked list, check if the linked list has a loop (cycle) or not.
# A loop means that the last node of the linked list is connected back to a node in the same list.

# Input: head: 1 -> 3 -> 4 -> 3
# Output: true

# Input: head: 1 -> 8 -> 3 -> 4 -> NULL 
# Output: false

class LinkedList:
    def __init__(self,data):
        self.data = data
        self.next = None


head = LinkedList(1)
head.next = LinkedList(3)
head.next.next = LinkedList(4)
head.next.next.next = LinkedList(5)
# head.next.next = LinkedList(4)
head.next.next.next.next = head

def show_linked_list(input:LinkedList):
    current = head
    output = ""

    while current:
        output = output + f'{current.data}->'
        print("outputtt", output)
        current = current.next

    output = output + f'->NULL'
    return output


# print("helllll", show_linked_list(head) )

def detect_loop(input:LinkedList):

    is_loop = False
    slow = head
    fast = head.next

    while fast and fast.next:
        print("slowww", slow.data, "fastt", fast.data)
        if slow == fast:
            is_loop = True
            return is_loop
        
        slow = slow.next
        fast = fast.next.next




    return is_loop

print(detect_loop(head))