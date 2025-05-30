# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution,
#  and you may not use the same element twice.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def two_sum(nums,target):
    dictionary = {}
    for index ,num in enumerate(nums):
        complement = target - num

        # print("indexxxxx", index)

        if complement in dictionary:
            # print("complementss", dictionary[complement], index)
            return[ dictionary[complement],index ]

        dictionary[num] = index

    return []

print(two_sum([2,11,7,15],9))