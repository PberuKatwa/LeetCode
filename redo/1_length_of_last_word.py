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

def length_of_last_word(s:str):
    output = 0
    tot_length = len(s)
    length = tot_length - 1

    while length > 0:

        if output > 0 and s[length] == " ":
            return output
        
        if s[length] != " " :
            
            output +=1

        length -= 1

    return output

print("lengthhhh", length_of_last_word("Hello World ") )
print("lengthhhh", length_of_last_word("   fly me   to   the moon  ") )