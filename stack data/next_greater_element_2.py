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

        print("indexxx", i)

        if stack:
            print("indexxx", i, array[ i ], ">>",  array[ stack[-1] ], "outputt", output)

        while stack and (  array[ i ] > array [ stack[-1] ] ):
            print("bff ...", stack, output)
            popped = stack.pop()
            output[popped] = array[i]
            print("aff ...", stack, output)


        stack.append(i)
            
        print("stack final", stack, "output", output)



    return output

print( next_greater_element( [4,5,2,25,2] ) )