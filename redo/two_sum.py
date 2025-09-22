# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution,
#  and you may not use the same element twice.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def two_sum(nums:list,target:int) -> list:
    map = {}
    i = 0
    for num in nums:
        complement = target - num

        print("mapp", map.get(complement))
        if map.get(complement) is not None:

            return [ map[complement] , i ]
        
        map[num] = i
        i += 1

    return []

print("summ", two_sum( [2,7,11,15], 18 ) )