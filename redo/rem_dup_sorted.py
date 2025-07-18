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

# def remove_duplicates(array:list) -> list:

#     length = len(array)
#     n = 0
#     k = length
#     length_2 = len(array)

#     while length - 1 :
#         length -= 1

#         p_a = n
#         p_b = n + 1

#         n += 1

#         if array[p_a] == array[p_b]:
#             k -= 1
#             print("pa", array[p_a], "pb",array[p_b],"b",p_b,array)
#             array[p_b] = array[p_b + 1] if p_b <= length else 0
#             print("nww arr",array )

#         print("lengthh", length, "pa", p_a, p_b)


#     return k,array

def remove_duplicates(array:list) -> list:

    length = len(array)
    n = 1
    k = length
    length_2 = len(array)

    for i in range( n , length ):

        if array[i] != array[i -1]:
            print('i', array[i], "i - 1 ", array[i -1], "arr", array  )
            array[n] = array[i]
            n += 1
            print("fin arr", array  )


    return n,array

print("finall list", remove_duplicates([0,0,1,1,3]))