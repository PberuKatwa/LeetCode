# Given a singly linked list, the task is to remove every kth node of the linked list.
# Assume that k is always less than or equal to the length of the Linked List.

# Examples : 
# Input: LinkedList: 1 -> 2 -> 3 -> 4 -> 5 -> 6, k = 2
# Output: 1 -> 3 -> 5 
# Explanation: After removing every 2nd node of the linked list, 
# the resultant linked list will be: 1 -> 3 -> 5 .

# Input: LinkedList: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10, k = 3
# Output: 1 -> 2 -> 4 -> 5 -> 7 -> 8 -> 10
# Explanation: After removing every 3rd node of the linked list,
# the resultant linked list will be: 1 -> 2 -> 4 -> 5 -> 7 -> 8 -> 10.

class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_kth_node(head, k):
    if not head or k <= 0:
        return head
    
    # Create a dummy node to handle edge cases
    dummy = LinkedList(0)
    dummy.next = head
    prev = dummy
    current = head
    count = 1  # 1-based counting
    
    while current.next is not None:
        if count % k == 0:
            # Remove the k-th node
            prev.next = current.next
            current = current.next
            print("no mod",current.data, "prevv", prev.data)
        else:
            # Move to next node normally
            prev = current
            current = current.next
            print("moddd ",current.data, "prevv", prev.data)

        count += 1
        print("dummyyy", dummy.data)
    
    return dummy.next

# Helper function to print the linked list
def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Create a linked list: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
head = LinkedList(0)
head.next = LinkedList(1)
head.next.next = LinkedList(2)
head.next.next.next = LinkedList(3)
head.next.next.next.next = LinkedList(4)
head.next.next.next.next.next = LinkedList(5)
head.next.next.next.next.next.next = LinkedList(6)
head.next.next.next.next.next.next.next = LinkedList(7)

print("Original list:")
print_list(head)

# Remove every 2nd node
new_head = remove_kth_node(head, 2)
print("\nAfter removing every 2nd node:")
print_list(new_head)