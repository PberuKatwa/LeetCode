class ListNode:
    def __init__(self, value):
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
    
    def remove_duplicates(self):
        current = self
        while current and current.next:
            if current.value == current.next.value:
                current.next = current.next.next
            else:
                current = current.next
        return self

# Helper function to create linked lists from arrays
def create_linked_list(values):
    """Create a linked list from a list of values"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Example usage and testing
if __name__ == "__main__":
    print("=== Testing Linked List Implementation ===\n")
    
    # Test Case 1: [1,1,2,3,3]
    print("Test 1: [1,1,2,3,3]")
    list1 = create_linked_list([1, 1, 2, 3, 3])
    print("Original:", list1.print_list())
    list1.remove_duplicates()
    print("After removing duplicates:", list1.print_list())
    print()
    
    # Test Case 2: [1,2,2,3,3,5]
    print("Test 2: [1,2,2,3,3,5]")
    list2 = create_linked_list([1, 2, 2, 3, 3, 5])
    print("Original:", list2.print_list())
    list2.remove_duplicates()
    print("After removing duplicates:", list2.print_list())
    print()
    
    # Test Case 3: Single element
    print("Test 3: [5]")
    list3 = create_linked_list([5])
    print("Original:", list3.print_list())
    list3.remove_duplicates()
    print("After removing duplicates:", list3.print_list())
    print()
    
    # Test Case 4: Empty list
    print("Test 4: []")
    list4 = create_linked_list([])
    if list4:
        print("Original:", list4.print_list())
        list4.remove_duplicates()
        print("After removing duplicates:", list4.print_list())
    else:
        print("Empty list - nothing to process")
    print()
    
    # Test Case 5: All duplicates
    print("Test 5: [2,2,2,2,2]")
    list5 = create_linked_list([2, 2, 2, 2, 2])
    print("Original:", list5.print_list())
    list5.remove_duplicates()
    print("After removing duplicates:", list5.print_list())