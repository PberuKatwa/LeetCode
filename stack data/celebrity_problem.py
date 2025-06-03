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

def find_celebrity(matrice):

    n = len(matrice)
    i = 0
    candidate = 0
    stack = list(range(n))
    print("nnn", n)
    print("matrice", matrice[1][0], matrice[1])

    while len(stack) > 1:
        i = i + 1

        print("stackkk before pop",stack, "cycle", i)

        a = stack.pop()
        b = stack.pop()

        print("stackkk after pop", stack )


        print("aa", a, "bbb", b)


        if matrice[a][b] == 1:
            print("atartt mat aaa bbb",matrice[a][b], matrice[a])
            stack.append(b)
        else:
            print("22222 ",matrice[a][b], matrice[a])
            stack.append(a)

        print("stackk after appending", stack)

    if not stack:
        return -1

    candidate = stack.pop()
    print("candidateee", candidate)

    for i in range(n):
        print("iiii", i, "cann", candidate)
        if i != candidate and (matrice[i][candidate] != 1 or matrice[candidate][i] == 1):
            return -1
        
    return candidate

   




    return

print("findddd",find_celebrity ( [[1, 1, 0], 
                                [0, 1, 0], 
                                [0, 1, 1]] ) )