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
    def __init__(self,data):
        self.data = data
        self.next = None

head = LinkedList(0)
head.next = LinkedList(1)
head.next.next = LinkedList(2)
head.next.next.next = LinkedList(3)
head.next.next.next.next = LinkedList(4)
head.next.next.next.next.next = LinkedList(5)
head.next.next.next.next.next.next = LinkedList(6)
head.next.next.next.next.next.next.next = LinkedList(7)

current = head
# linked_array = []
while current:
    # print("this is the headd", current.data)
    # linked_array.append(current.data)
    current = current.next

def remove_kth_node(list:LinkedList,interval):

    n = 1
    linked_array = []
    current_list = ''
    
    dummy = LinkedList(0)
    
    current_head = list
    previous_head = None
    while current_head is not None:

        if(current_head.data == None):
            return None

        
        print("index",n ,"headddd", current_head.data, "array", linked_array)
        modulus = n % interval
        
        if n!=0 and modulus == 0:

            current_head = current_head.next.next 
            print("nonn modulusss",current_head.data)

        else:

           current_head = current_head.next 

        current_list = current_list + f'{current_head.data} -> '
        linked_array.append(current_head.data)
        n = n + 1

        print("currentttt listt", current_list)


    return current_list


print("linked list functionnn",remove_kth_node(head,2))
