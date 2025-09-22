# Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
# Return the linked list sorted as well.

# Input: head = [1,1,2]
# Output: [1,2]

# Input: head = [1,1,2,3,3]
# Output: [1,2,3]

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self ):
        self.head = None

    def create_list(self, value):
        if self.head is None:
            self.head = ListNode(value)

        else:
            current = self.head

            while current.next:
                current = current.next

            current.next = ListNode(value)

        return self.head
        
    def print_list(self) -> str:
        output = ""
        current = self.head

        while current:
            output += f'{current.value}->'
            current = current.next

        output += "NULL"
        return output
    
    def remove_duplicates(self) :
        current = self.head

        while current and current.next:
            if current.value == current.next.value:
                current.next = current.next.next

            current = current.next

        return self.head
    
    def create_list_array(self, array:list):
        if self.head is None:
            self.head =  ListNode( array[0] )

        current = self.head

        for item in array[1:]:
            current.next = ListNode(item)
            current =  current.next

        return self.head
    
head = LinkedList()
head.create_list_array( [1,1,2,3,3] )
head.remove_duplicates()

print("headd", head.print_list() )


    