# You are given two non-empty linked lists representing two non-negative integers.
#  The digits are stored in reverse order, and each of their nodes contains a single digit.
#  Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

class ListNode:
    def __init__( self, value:int ):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def create_list_array(self, array:list):
        if self.head is None:
            self.head = ListNode ( array[0] )

        current = self.head

        for item in array[1:]:
            current.next = ListNode( item )
            current =  current.next

        return self.head
    
    def print_linked_list(self):
        output = ''
        current = self.head

        while current:
            output +=f'{current.value} -> '
            current = current.next

        output +="NULL"
        return output
    
    def reverse_list_to_int(self) -> int:
        number = 0

        current = self.head

        n = 0
        while current:
            place_value = 10 ** n
            number += (current.value) * ( place_value )
            n +=1
            current = current.next

        return number
    

list_a = LinkedList()
list_a.create_list_array([2,4,3])

list_b = LinkedList()
list_b.create_list_array([5,6,4])

def add_reverse_linked_list(list_a:LinkedList, list_b:LinkedList) -> LinkedList:
    total = 0
    dummy = LinkedList()
    carry = 0
    
    current = LinkedList()
    current.head = ListNode( 0 )
    current_2 = current.head
    p1 = list_a.head
    p2 = list_b.head

    while p1 or p2 or carry:
        num_1 =  p1.value if p1 else 0 
        num_2 =  p2.value if p2 else 0 

        total = num_1 + num_2 + carry
        carry = total // 10
        modulus = total % 10
        print("num_1", num_1, "num_2", num_2, "totall", total)
        print("modulus", modulus, "absolute divisor", carry)

        current_2.next = ListNode(modulus)
        current_2 = current_2.next

        print(" cureeent", current.print_linked_list())


        if p1:
            p1 = p1.next

        if p2:
            p2 = p2.next



    dummy.head = current.head.next
    return dummy

# print("listtt aa", list_a.print_linked_list())
# print("nummm aa", list_a.reverse_list_to_int() )

# print("listtt bb", list_b.print_linked_list())
# print("nummm bb", list_b.reverse_list_to_int() )

dummy = add_reverse_linked_list(list_a,list_b)

print("TOTALLLL", dummy.print_linked_list() )