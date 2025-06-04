# Given an array, find the next greater element (NGE) for every element.
# If no greater element exists, return -1.

# Example:
# Input: [4, 5, 2, 25]
# Output: [5, 25, 25, -1]

def next_greater_element(array:list):

    greatest = 0
    output = [-1] * len(array)
    stack = []

    for i in range( len( array ) ):

        if stack:
            print("indexxx", i, "stackkk", array[ stack[-1] ], "arr",  array[i], "outputt", output)

        while stack and array[ stack[-1] ] < array[i]:

            popped_index = stack.pop()
            output[popped_index] = array[i]
            print(f"Popped {popped_index}, updated output[{popped_index}] = {array[i]}, outt {output}")

        stack.append(i)  
        print(f"Stack after processing index {i}: {stack}")

    return output

print( next_greater_element( [4,5,2,25] ) )