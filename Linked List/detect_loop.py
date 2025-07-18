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
head.next.next.next = head

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

    prev = head
    print("prevv data", prev.data)
    current = head.next
    print("current",current.data)
    nxt = current.next
    is_loop = False

    while current:
        
        if prev == current.next:
            print(f'prevvvv {prev.data}, current {current.data}')
            is_loop = True
            return is_loop
        else:
            print("were else", current.data, "prevv", prev.data)
            prev = current
            current = current.next

            if current.next is None:
                prev = nxt
                current = nxt.next




    return is_loop

print(detect_loop(head))