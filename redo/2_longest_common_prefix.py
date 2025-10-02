# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


def longest_common_prefix(strs: list) -> str:
    if not strs:
        return ""

    initial = strs[0]           # prefix candidate
    for item in strs[1:]:
        i = 0
        # only compare up to the shorter of the two strings
        limit = min(len(initial), len(item))
        consecutive = ""       # MUST reset for each item
        while i < limit and initial[i] == item[i]:
            consecutive += initial[i]
            i += 1
        initial = consecutive  # shrink the candidate
        if not initial:        # early stop if nothing common
            return ""

    return initial

print(longest_common_prefix(["flower","flow","flight"]))  # -> "fl"
