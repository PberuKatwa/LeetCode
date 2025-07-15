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
    n = -1
    t = 0
    found = False
    found_occurrence = 0

    while found_occurrence < 1:

        if ( s[n] == " " ) and not found :
            print("emptyyyy", s[n])

        if ( s[n] != " " ):
            found = True
            t = t + 1 
            print("founddd", s[n], t)

        n = n - 1
        print("indexxx", s[n], t)

        if ( t > 1 ) and ( s[n] == " " ):
            found_occurrence = found_occurrence + 1
            found = False


    return t



# print( length_last_word("   fly me   to   the moon  ") )
print( length_last_word("luffy is still joyboy") )