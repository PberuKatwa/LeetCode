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

    total_length = len(s)
    n = 0
    t = 0
    found = False
    found_occurrence = 0

    while ( found_occurrence < 1 ) and ( abs(n) < total_length ) :
        print("nnnn", n, total_length)
        n = n - 1

        if ( s[n] != " " ):
            t = t + 1 

        if ( t > 1 ) and ( s[n] == " " ):
            found_occurrence = found_occurrence + 1

        



    return t



# print( length_last_word("   fly me   to   the moon  ") )
# print( length_last_word("luffy is still joyboy") )
# print( length_last_word("y ") )
print( length_last_word(" abc ") )