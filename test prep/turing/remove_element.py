# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The order of the elements may be changed. Then return the number of elements in nums which are not equal
# to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted,
# you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
# The remaining elements of nums are not important as well as the size of nums.
# Return k.

# Example 1:

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).


def remove_elem_place( nums:list, val:int ) -> tuple[ int, list ]:

    if ( len(nums) < 1 ) or ( val is None ):
        return 0

    k = 0
    p_a = 0
    p_b = len(nums) - 1

    while p_a < len(nums):

        if nums[p_a] != val:
            k += 1

            while nums[p_b] == val:
                p_b -= 1

            nums[p_a] = nums[p_b]

        if ( p_a + 1 ) == p_b:
            p_a =+ 2

        p_a += 1

    return k, nums

print("resss", remove_elem_place( [3,2,2,3], 3 ) )