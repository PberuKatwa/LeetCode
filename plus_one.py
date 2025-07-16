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

def plus_one(digits:list):
    place_value = len(digits) - 1
    print("diggg", digits)
    full_no = 0
    no_digits = 0
    original = digits

    for index,digits in enumerate(digits):
        print("full no", full_no, "place", place_value, "index", index)
        full_no = full_no + ( digits * ( 10 ** place_value ) )
        place_value -=1 

    full_no_str = len( str( full_no + 1 ) )
    str_2 = str(full_no + 1)

    print( "len str", full_no_str, place_value+1, original, str_2 )
    n = len(original)
    if ( n == 1 ) and ( full_no_str != n ):
        first = original[n-1]
        return

    return full_no + 1

print(plus_one([9]))