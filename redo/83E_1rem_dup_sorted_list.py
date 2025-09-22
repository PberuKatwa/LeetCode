# Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
# Return the linked list sorted as well.

# Input: head = [1,1,2]
# Output: [1,2]

# Input: head = [1,1,2,3,3]
# Output: [1,2,3]

class LinkedList:
    def __init__(self, value ):
        self.value = value
        self.next = None
        
    def print_list(self) -> str:
        output = ""
        current = self

        while current:
            output += f'{current.value}->'
            current = current.next

        output += "NULL"
        return output
    
    def remove_duplicate(self) :
        current = self

        while current and current.next:
            if current.value == current.next.value:
                current.next = current.next.next

            current = current.next

        return self
    

head = LinkedList(1)
head.next = LinkedList(1)
head.next.next = LinkedList(2)
head.next.next.next = LinkedList(3)
head.next.next.next.next = LinkedList(3)

head.remove_duplicate()

head_2 = LinkedList(1)
head_2.next = LinkedList(2)
head_2.next.next = LinkedList(2)
head_2.next.next.next = LinkedList(3)
head_2.next.next.next.next = LinkedList(3)
head_2.next.next.next.next.next = LinkedList(5)

print( "listtttt", head.print_list() )
print( "listtttt", head_2.remove_duplicate().print_list() )
