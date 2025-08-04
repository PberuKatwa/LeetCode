# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
# representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

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

class Solution:
    def __init__( self, nums1:list, nums2:list, m:int, n:int )->list:
        self.nums1 = nums1
        self.nums2 = nums2
        self.m = m
        self.n = n

    def merge_sorted_list(self):
        n=0
        i=0
        t = self.m + self.n
        f=0
        # while ( self.nums1[n] < self.m ) and ( self.nums2[i] < self.n ):

        #     # print("befff","list",self.nums1)
        #     print("befff","list", self.nums1, "n", n, "n list", self.nums1[n], "i", i, self.nums2[i]   )

        #     if self.nums1[n] <= self.nums2[i]:
        #         print("herre 1 <<< 2", "list1=", self.nums1[n], "list2=", self.nums2[i],"nnn",n,"iii",i)
        #         i += 1
        #     else:
        #         print("herre 1 <<< 2", "list 1", self.nums1[n], "list 2", self.nums2[i],"nnn",n)
        #         self.nums1.insert(n,self.nums2[i])
        #         print("numsssss",  self.nums1)
        #         n +=1

        #     # print("affff","list", self.nums1, "n", n, "n list", self.nums1[n], "i", i, self.nums2[i]   )

        if self.m >= self.n:
            print("hereee")
            while self.nums1[n] <= t:

                if self.nums1[n] <= self.nums2[i]:
                    print("1 <<< 2", "list1=", self.nums1[n], "list2=", self.nums2[i],"nnn",n,"iii",i, "fff",f)
                    n += 1

                if self.nums1[n] > self.nums2[i]: 
                    print("1 >>> 2", "list 1", self.nums1[n], "list 2", self.nums2[i],"nnn",n,"ff",f)
                    self.nums1.insert(f,self.nums2[i])
                    i += 1 
                
                print("affff","list", self.nums1, "n", n, "n list", self.nums1[n], "i", i, self.nums2[i]   )
                f = i + n + 1

            print("iiii",n, "ttt",t)
        return self.nums1
    
sort_list = Solution([1,2,3,0,0,0],[2,5,6],3,3)

print("ansss", sort_list.merge_sorted_list())