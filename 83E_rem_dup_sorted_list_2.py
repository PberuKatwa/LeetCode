# Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
# Return the linked list sorted as well.

# Input: head = [1,1,2]
# Output: [1,2]

# Input: head = [1,1,2,3,3]
# Output: [1,2,3]

class LinkedList:
    def __init__(self,value):
        self.value = value
        self.next = None

    def print_linked_list(self):
        output = ""
        current = self

        while current is not None:
            output += f'{current.value}->'
            current = current.next

        output +="null"
        return output
    
    def remove_duplicates(self):

        current =  self

        while current and current.next is not None:

            if current.value == current.next.value:
                current.next = current.next.next

            current = current.next

        return self


        



    
head = LinkedList(1)
head.next = LinkedList(1)
head.next.next = LinkedList(2)
head.next.next.next = LinkedList(2)
head.next.next.next.next = LinkedList(3)

head.remove_duplicates()

print("listt", head.print_linked_list() )

        

        