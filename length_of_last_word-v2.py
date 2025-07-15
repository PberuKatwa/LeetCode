# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.

def length_last_word(s:str):

    n = len(s) - 1
    t = 0

    while ( n > 0 ) and ( s[n] == " " ) :
        n = n - 1

    while ( n > 0 ) and ( s[n] != " " ):
        t = t + 1
        n = n - 1

    return t



print( length_last_word("   fly me   to   the moon  ") )
# print( length_last_word("luffy is still joyboy") )
# print( length_last_word("y ") )
# print( length_last_word(" abc   ") )