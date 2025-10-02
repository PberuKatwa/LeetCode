# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

def longest_common_prefix(list:list):

    initial = list[0]
    list.pop(0)
    consecutive = ""
    print("initialll",initial)
    for item in list:
        index = 0
        n = len(item) 
        print("itemm", item)
        print("n", n)
        print("itemm index", item[index])
        
        while (index < n) and ( initial[index] == item[index] ):
            print ("itemmm", initial[index] , "itt", item[index])
            consecutive = consecutive + initial[index]
            print("consecutiveee",consecutive)
            index = index + 1


    return consecutive

print("ansss",longest_common_prefix(["flower","flow","flight"]))