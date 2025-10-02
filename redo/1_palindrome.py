# Given an integer x, return true if x is a palindrome, and false otherwise.

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

def is_palindrome(x:int) -> bool:
    new_num = x
    fin_num = 0

    while x > 0:
        fin_num = ( fin_num * 10 ) + new_num % 10
        new_num = new_num // 10

        if( fin_num == x ):
            return True
 

    return False

print("palll", is_palindrome(12))