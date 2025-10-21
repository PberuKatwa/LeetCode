# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
# representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
#  To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that
#  should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

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

def merge_sorted_lists( nums_1:list, nums_2:list, m:int, n:int ) -> list :

    total = m + n
    pointer_a = m - 1 if m > 0 else 0
    pointer_b = n - 1 if n > 0 else 0
    pointer_c = total - 1

    while pointer_c >= 0:

        print("numss", nums_1)

        if( nums_1[ pointer_a ] >= nums_2[pointer_b] ):
            nums_1[ pointer_c ] = nums_1[ pointer_a ]
            pointer_a -= 1
        else:
            nums_1[ pointer_c ] = nums_2[ pointer_b ]
            pointer_b -= 1

        pointer_c -=1



         

    return nums_1

# print("listttt", merge_sorted_lists( [1,2,3,0,0,0], [2,5,6], 3, 3  ) )
# print("listttt 222", merge_sorted_lists( [1], [], 1, 0  ) )
print("listttt 222", merge_sorted_lists( [0], [1], 0, 1  ) )
            
