# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
#  and two integers m and n,
# representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function,
#  but instead be stored inside the array nums1.
#  To accommodate this, nums1 has a length of m + n,
#  where the first m elements denote the elements that should be merged,
#  and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
# Example 2:

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].
# Example 3:

# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1.
# The 0 is only there to ensure the merge result can fit in nums1.

def merge_sorted_list(nums_1:list, m:int, nums_2:list, n:int) -> list:

    if( len(nums_1) < 1 ) or ( len(nums_2) < 1 ) or ( m is None ) or ( n is None ):
        return [] 

    p_1 = m - 1
    p_2 = n - 1
    i = len(nums_1) - 1

    while ( p_1 >= 0 ) and ( p_2 >= 0 ) :
        print( "\n1111", p_1, nums_1[p_1], "2222", p_2, nums_2[p_2], "iiii", i )
        print("beforee list", nums_1)

    
        if nums_1[p_1] >= nums_2[p_2]:
            print("111 p1 > p2", nums_1[p_1] ,">>", nums_2[p_2] )
            nums_1[i] = nums_1[p_1]
            p_1 -= 1

        else:
            print("222 p2 > p1", nums_2[p_2] ,">>", nums_1[p_1] )
            nums_1[i] = nums_2[p_2]
            p_2 -= 1

        print("numss 11", nums_1, "iii", i)
        i -= 1

    print("\np1", p_1, "p_2", p_2, "iii", i)

    while p_2 >= 0:
        print("\nlisttt", nums_1, "p2", p_2)
        nums_1[i] = nums_2[p_2]
        p_2 -= 1
        i -= 1

    return nums_1

# print("numss Ans", merge_sorted_list( [1,2,3,0,0,0], 3, [2,5,6], 3 ) )
print("numss Ans", merge_sorted_list( [4,5,6,0,0,0] , 3, [1,2,4], 3 ) )