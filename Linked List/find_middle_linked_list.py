# Given a singly linked list, the task is to find the middle of the linked list.
#  If the number of nodes are even, then there would be two middle nodes, so return the second middle node.

# Example:

# Input: linked list: 1->2->3->4->5
# Output: 3 
# Explanation: There are 5 nodes in the linked list and there is one middle node whose value is 3.

# Input: linked list = 10 -> 20 -> 30 -> 40 -> 50 -> 60
# Output: 40
# Explanation: There are 6 nodes in the linked list, 
# so we have two middle nodes: 30 and 40, but we will return the second middle node which is 40.
import math

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

def show_linked_list(list_input:LinkedList):
    current = list_input
    list_output = ""
    while current:
        list_output = list_output + f'{current.data} -> '
        current = current.next
        # print("current list", list_output)

    
    return list_output


print("listtt", show_linked_list(head))

def find_middle_node(list_input:LinkedList):

    if list_input is None:
        return f'no data'


    current = list_input
    n = 0
    list_map = {}
    middle_node = ''

    while current:
        n = n + 1
        list_map[n]=current.data
        current  = current.next

    middle_n = n/2

    if n % 2 == 0:
        first_node = list_map[middle_n]
        second_node = list_map[ ( middle_n + 1 ) ]
        middle_node = middle_node + f' {first_node} , {second_node} '
    else:
        node = list_map[math.ceil(middle_n)]
        middle_node = middle_node + f' {node} '

    return middle_node

print("middle nodeee", find_middle_node(head))





