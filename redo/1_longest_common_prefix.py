# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


def longest_common_prefix(strs:list) ->str:
    if not strs:
        return ""
    
    prefix_string = ''
    start_str = strs[0]

    for item in strs[1:]:
        print("itemm", item)
        index = 0
        n = len(item)

        prefix_string = ""
        while( n > index ) and ( start_str[index] == item[index]  ):
            prefix_string += item[index]
            print("heree", item[index], "preff", prefix_string)

            index +=1


        start_str = prefix_string


    return prefix_string

print("longest common prefix", longest_common_prefix(["flower","flow","flight"]))