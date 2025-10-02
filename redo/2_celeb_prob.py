# Given a square matrix mat[][] of size n x n, such that mat[i][j] = 1 means ith person knows jth person,
#  the task is to find the celebrity. A celebrity is a person who is known to all but does not know anyone.
#  Return the index of the celebrity, if there is no celebrity return -1.

# Note: Follow 0-based indexing and mat[i][i] will always be 1.

# Examples:  

# Input: mat[][] = [[1, 1, 0], 
#                   [0, 1, 0], 
#                   [0, 1, 1]]
# Output: 1
# Explanation: 0th and 2nd person both know 1. Therefore, 1 is the celebrity.

# Input: mat[][] = [[1, 1], 
#                  [1, 1]]
# Output: -1
# Explanation: The two people at the party both know each other. None of them is a celebrity.

# Input: mat[][] = [[1]]
# Output: 0

def find_celebrity(matrice:list) -> int:
    stack = list(range( len(matrice) ))
    candidate = 0

    while len( stack ) > 1:
        print("stackkk", stack)
        person_a = stack.pop()
        person_b = stack.pop()

        print("stackkk", stack)
        print("pers aa", person_a, "pers b", person_b)

        if matrice[person_a][person_b] == 1:
            print("hereee at knows ")
            stack.append(person_b)
        else:
            print("NOOOOO ")
            stack.append(person_a)
            
        print("stackkkk", stack)

    if not stack:
        return -1
    
    candidate = stack.pop()

    n = len(matrice)

    for i in range(n):

        if candidate == i:
            continue

        if matrice[candidate] [i] == 1:
            return -1
        elif( matrice[i][candidate] == 0 ):
            return -1


    return candidate

print("celebbb", find_celebrity([[1, 1, 0], 
                                [0, 1, 0], 
                                [0, 1, 1]]) )
