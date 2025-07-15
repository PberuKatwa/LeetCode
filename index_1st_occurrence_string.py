# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.

# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

def first_occurrence(haystack:str,needle:str):
    n = 1
    t = len(needle)

    for i in range(1 , len(haystack)):

        print(haystack[i-1],"needle", needle[n], "iiiiii", i)

        while n <= len(needle) and ( needle[n-1] == haystack[i-1] ) :
            print( "needle",needle[n-1],"hayyy",haystack[i-1], "nnn", n )
            n = n + 1
            # print("needle", needle,"lenn", len(needle))

    return 

print("firstt", first_occurrence("adbutsad","sad"))