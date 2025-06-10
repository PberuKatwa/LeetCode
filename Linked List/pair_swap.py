# Given a singly linked list, the task is to swap linked list elements pairwise.

# Examples:

# Input : 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL 
# Output : 2 -> 1 -> 4 -> 3 -> 6 -> 5 -> NULL

# Input : 1 -> 2 -> 3 -> 4 -> 5 -> NULL 
# Output : 2 -> 1 -> 4 -> 3 -> 5 -> NULL

class LinkedList:
    def __init__(self,data):
        self.data = data
        self.next = None

head = LinkedList(1)
head.next = LinkedList(2)
head.next.next = LinkedList(3)
head.next.next.next = LinkedList(4)
head.next.next.next.next = LinkedList(5)
head.next.next.next.next.next = LinkedList(6)

def show_linked_list(head:LinkedList):
    current = head
    list_output = ""

    while current:
        list_output = list_output + f'{current.data} -> '
        current = current.next



    return list_output

# print(show_linked_list(head))

def pair_swap(head:LinkedList):

    current = head
    list_output = ""

    while current.next.next:
        print("starrt", current.data, current.next.data)
        now = current.data
        pair = current.next.data
        print("nowww", now, "pairr", pair)
        current.data = pair
        current.next.data = now
        current.next = current.next.next
        print("current", current.data, "next", current.next.data)

    return current


head_2 = pair_swap(head)
print(show_linked_list(head_2))
print(show_linked_list(head))
