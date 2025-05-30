# Problem 1: Reverse a Linked List
# Real-World Analogy: Rewinding a cassette tape (remember those?). You need to flip the order of songs.

# Task: Given a singly linked list, reverse it in-place.

# class LinkedList:
#     def __init__(self,title):
#         self.title = title
#         self.next = None
#         self.previous = None


# def reverse_list(object:list):

#     for item in object:



#         print("itemmm ", item)

#     pass

# print("reverse list", reverse_list( [1,2,3,4] ) )

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_temp = current.next  # Save next node
        current.next = prev       # Reverse the link
        prev = current            # Move prev forward
        current = next_temp       # Move current forward
    return prev  # New head

print("reverse linked list",reverse_linked_list([1,2,3,4]))