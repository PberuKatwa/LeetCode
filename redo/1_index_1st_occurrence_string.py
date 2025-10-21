# Given two strings needle and haystack,
# return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.

# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

def index_1st_occurrence( needle:str, haystack:str ) -> int:

    ndl_length = len(needle) -1
    hay_length = len(haystack) -1
    n = 0
    output = 0

    while n <= hay_length:
        tot_index = n + ndl_length + 1
        if needle == haystack[n:tot_index] :
            return n

        n += 1

    return None

print( index_1st_occurrence( "sad", "adbutsad" ) )

