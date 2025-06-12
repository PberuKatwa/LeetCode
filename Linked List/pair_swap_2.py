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


    list_output += "NULL"
    return list_output

# print(show_linked_list(head))

def pair_swap(head:LinkedList):

    current = head
    new_head = head.next
    prev = None

    while current and current.next:

        print("current 11", current.data, "neww head", new_head.data)

        nxt = current.next
        next_pair = nxt.next

        nxt.next = current
        current.next = next_pair

        if prev:
            prev.next = nxt
            print("prevv", prev.data)


        prev = current
        current = next_pair
        # print("current", current.data, "neww head", new_head.data)

    return new_head


head_2 = pair_swap(head)
print(show_linked_list(head_2))
# print(show_linked_list(head))
