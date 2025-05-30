# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list.
# The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]

class LinkedList:
    def __init__(self,data):
        self.data = data
        self.next = None
        pass

def create_linked_list(array:list):
    head = LinkedList(array[0])
    current = head
    array.pop(0)

    for item in array:
        current.next = LinkedList(item)
        current = current.next

    return head

def show_linked_list(list_input:LinkedList):
    current = list_input
    list_output = ""

    while current:
        list_output = list_output + f"{current.data} -> "
        current = current.next

    return list_output

head_1 = create_linked_list([1,2,4])
head_2 = create_linked_list([1,3,5])

# print("linked list", show_linked_list(head_1))
# print("linked list", show_linked_list(head_2))

def merge_two_sorted_list(list_1:LinkedList,list_2:LinkedList):

    dummy = LinkedList(0)
    sorted_head = dummy
    current = sorted_head

    while list_1 and list_2 is not None:
        if list_1.data >= list_2.data:

            current.next = list_2
            list_2 = list_2.next
        else:

            current.next = list_1
            list_1 = list_1.next

        current = current.next

    if list_1:
        current.next = list_1
    else:
        current.next = list_2

    return sorted_head.next

sorted =  merge_two_sorted_list(head_1,head_2)

print(show_linked_list(sorted))




