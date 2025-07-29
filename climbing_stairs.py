# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

class Solution:
    def __init__(self , n:int ):
        self.n = n
        self.one_step = None
        self.two_steps = None

    def climbing_stairs(self):

        modulus = self.n % 2
        div = self.n // 2

        self.one_step = ( div * 2 ) + modulus
        self.two_steps = div + modulus

        return {
            "one_step":self.one_step,
            "two_step":self.two_steps
        }
    
    def no_of_ways(self):

        if self.n == 1:
            return 1
        
        if self.n == 2:
            return 2
        
        a = 1
        b = 2

        for i in range( 3 , self.n + 1 ):
            print("befff", a, "and b", b)
            current = a + b
            a = b
            b = current
            print("afff", "a", a, "bbb", b)

        

        return current
    
# stairs_1 = Solution( 5 ).no_of_ways()
stairs_2 = Solution( 15 ).no_of_ways()


# print( "climbing stairs 1 " , print(stairs_1) )
print( "climbing stairs 2 " , print(stairs_2) )