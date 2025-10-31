# Given an integer array nums sorted in non-decreasing order,
# remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same.
# Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k,
# to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements
# in the order they were present in nums initially. The remaining elements of nums are not
# important as well as the size of nums.

# Return k.

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

def rem_dup_sorted( nums:list ) -> tuple[ int, list ]:
    if len(nums) < 1:
        return 0
    
    p_a = 0
    p_b = 1
    k = 1

    while   p_b < len(nums) :

        print("\n AAA", p_a, nums[p_a] )
        print(" BBB", p_b, nums[p_b] )

        if nums[p_a] == nums[p_b]:
            print( "\n EQUALL", "A", p_a, nums[p_a], "B", p_b, nums[p_b] )
            p_b +=1
        else:
            print( "\n VALIDDD", "A", p_a, nums[p_a], "B", p_b, nums[p_b] )
            nums[ p_a + 1 ] = nums[ p_b ]
            k += 1
            p_a +=1
            p_b +=1
            print( "ENDD", "K", k )


    return k, nums

# print("duppp", rem_dup_sorted( [1,1,2] ) )
print("duppp", rem_dup_sorted( [0,0,1,1,1,2,2,3,3,4] ) )