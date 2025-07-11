# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.
# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4

def search_insert_position(nums: list, target: int) -> int:
    left = 0
    right = len(nums) - 1    
    
    while left <= right:
        mid = (left + right) // 2
        print("middd", left, right, mid, "numss", nums[mid])
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
            print("elifff", left)
        else:
            right = mid - 1
    
    return left


print(search_insert_position([1,3,5,6], target=7))