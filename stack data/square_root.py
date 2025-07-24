# Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
# The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator.
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
# Example 1:

# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.

# Example 2:
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., 
# and since we round it down to the nearest integer, 2 is returned.

def is_even_number(num:int) -> bool:

    if num % 2 != 0:
        return False

    return True

def calculate_square_root(x:int):

    left = 1
    right = x

    while right >= left:

        mid = ( left + right ) // 2
        print("midd", mid)

        sqr = mid * mid

        if sqr == x:
            return mid
        elif sqr < x:
            left = mid + 1
            print("less than", mid ,"leff", left ,"rtt",sqr ,"xxx", x )
        else:
            right = mid - 1
            print("more than", mid, "righh", right, "rttt", sqr,"xxx", x )

    return

print("calcc", calculate_square_root(81))