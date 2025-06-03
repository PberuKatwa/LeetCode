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

def find_celebrity(mat):
    n = len(mat)
    stack = list(range(n))
    
    # Narrow down the candidate using the stack
    while len(stack) > 1:
        a = stack.pop()
        b = stack.pop()
        
        if mat[a][b] == 1:
            # a knows b, so a cannot be the celebrity
            stack.append(b)
        else:
            # a does not know b, so b cannot be the celebrity
            stack.append(a)
    
    if not stack:
        return -1
    
    candidate = stack.pop()
    
    # Verify the candidate
    for i in range(n):
        if i != candidate and (mat[i][candidate] != 1 or mat[candidate][i] == 1):
            return -1
    
    return candidate

print("findddd",find_celebrity ( [[1, 1, 0], 
                                [0, 1, 0], 
                                [0, 1, 1]] ) )