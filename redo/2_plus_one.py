# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit
#  of the integer. The digits are ordered from most significant to least significant in left-to-right order.
#  The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.
# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
# Example 3:

# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].

def plus_one(digits:list) -> list:
    output_list = []
    n = len(digits) - 1
    carry = 0
    add = 1

    while n >= 0:
        print("originall", digits)
        value = digits[n]
        total =  value + add + carry
        add = 0
        dig = total % 10
        carry = total // 10

        digits[n] = dig
        if carry == 0:
            return digits

        digits[n] = dig
        print("dig", digits[n], "digitsss", digits)
        n -=1

    print("carry",carry)
    return [1] + digits


print("plusss", plus_one( [ 9, 9] ) )