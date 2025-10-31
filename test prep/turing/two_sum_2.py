# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution,
#  and you may not use the same element twice.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def two_sum(nums:list, target:int) -> list:

    if len(nums) < 1 or target is None:
        return []

    num_map = {}
    index = 0

    for num in nums:

        complement =  target - num

        if complement in num_map:
            return [ num_map[complement], index ]

        num_map[num] = index         
        index += 1

    return []

# print( "Solution" , two_sum( [2,7,11,15], 9 ) )
# print( "Solution 2" , two_sum( [2,7,11,15], 18 ) )
# print( "Solution 2" , two_sum( [3, 2, 4], 6 ) )
# print( "Solution 2" , two_sum( [5, 3, 1], 6 ) )
# print( "Solution 2" , two_sum( [1, 2, 3], 4 ) )
print( "Solution 2" , two_sum( [1, 4, 5, 6] , 11 ) )