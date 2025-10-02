# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

def is_common_prefix(length:int, strs:list):
    for original_index in range(length):
        original_char = strs[0][original_index]
        print("\n START","|| ORIGINAL CHAR =>", original_char, "itemm", original_index)


        for single_item in range( 1, len(strs) ):
            actual_item = strs[single_item]
            comparison_char = strs[single_item][original_index]
            print("\n || list_index =>",single_item, "|| actual =>", actual_item, "|| comparison char =>", comparison_char, "|| index =>", single_item )

            if comparison_char != original_char:
                return False

    return True

def longest_common_prefix(strs:list) ->str:
    if not strs:
        return ""
    
    prefix_string = ''
    start_str = strs[0]

    min_length = len(start_str)

    for item in strs[1:]:
        if len(item) < min_length:
            min_length = len(item)
    
    low = 0
    high = min_length
    while low <= high:
        mid = ( low + high ) // 2
        print("\n ==> START BINARY COMMON PREFIX", "|| MID :", mid)
        if is_common_prefix(mid, strs) :
            print("\n ==> SUCCESS BINARY COMMON PREFIX", "|| MID :", mid)
            low = mid + 1
        else:
            print("\n ==> FAIL BINARY COMMON PREFIX", "|| MID :", mid)
            high = mid - 1   
                 


    prefix_string = start_str[0:high]


    return prefix_string

print("longest common prefix", longest_common_prefix(["flower","flow","flight"]))