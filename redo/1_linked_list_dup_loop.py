# Given the head of a linked list.
# The task is to find the length of the loop in the linked list.
# If the loop is not present return 0.

# Examples:

# Input: head: 1  → 2  → 3  → 4  → 5  → 2
# Output: 4
# Explanation: There exists a loop in the linked list and the length of the loop is 4.

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def create_from_array( self, array:list):
        if self.head == None:
            self.head = ListNode(array[0])
        
        current = self.head

        for item in array[1:]:
            current.next = ListNode( item )
            current = current.next

        return self.head
    
    def create_loop(self):
        slow = self.head
        fast = self.head

        while fast.next and fast.next.next:

            slow = slow.next
            fast = fast.next.next

            if slow.value == fast.value :
                slow.next = ListNode(slow)


        return self.head
    
    def print_linked_list(self):
        output = ''
        current = self.head

        while current:
            output += f'{current.value}->'
            current = current.next
    
        output += f'->NULL'
        return output
    
    def check_loop_length(self):
        length = 0 

        slow = self.head
        fast = self.head

        while fast.next and fast.next.next:
            slow =  slow.next
            fast = fast.next.next

            if( slow == fast ):
                print("slowww",slow.value, "fasss", fast.value)


                loop_value = slow
                slow = slow.next
                length = 1
                while slow:
                    if slow != loop_value:
                        length += 1
                    else:
                        return length 
                    
                    slow =  slow.next

        return length
    

list_a = LinkedList()
list_a.create_from_array([1, 2, 3, 4, 5, 2])

list_b = LinkedList()
list_b.create_from_array([1, 2, 3, 4, 5, 2])
list_b.create_loop()

print("linked list", list_a.print_linked_list())
print("\n loop checkk", list_b.print_linked_list() )
