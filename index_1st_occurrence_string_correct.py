# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.

# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

def first_occurrence(haystack: str, needle: str) -> int:
    n = len(needle)
    h = len(haystack)
    
    if n == 0:
        return 0
    if n > h:
        return -1
    
    for i in range(h - n + 1):
        if haystack[i:i+n] == needle:
            print("hellooo", haystack[i:i+n], n, "iii", i, "i+n", i+n, )
            return i
    return -1


print("first occurrence", first_occurrence("adbutsad","sad"))