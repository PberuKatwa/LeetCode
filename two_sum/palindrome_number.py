# Given an integer x, return true if x is a palindrome, and false otherwise.

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

def is_number_palindrome(number:int):
    if number < 0:
        return False
    
    num_digits = len(str(number))
    new_value = number
    final_value = 0
    reversed_num = 0
    while int(new_value) > 0:
        digit = int (new_value % 10)
        # print("newww", new_value)
        print("newww", digit)
        reversed_num = (reversed_num * 10) + digit
        print("reversedd",reversed_num)
        new_value =  new_value / 10

        num_digits = num_digits - 1
        place_value = 10 ** num_digits
        palindrome = place_value * ( int ( (new_value * 10 ) % 10 ) )
        final_value = final_value + palindrome
        # print(new_value)
        # print("newww pal",palindrome)
        # print("final", final_value)



    return number == reversed_num

print("palindromeee", is_number_palindrome(323))