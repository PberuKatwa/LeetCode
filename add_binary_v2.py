# Given two binary strings a and b, return their sum as a binary string.

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

def convert_from_binary(input:str):
    n = len(input)
    decimal = 0 
    initial = 0

    for i in range( n - 1 , -1 , -1):
        base_2 = 2 ** initial
        initial += 1
        value = int( input[i] ) * base_2
        decimal += value

    return decimal

# print(convert_from_binary("1010"))

def add_binary( a:str , b:str) -> str:

    pointer_a = len(a) - 1
    pointer_b = len(b) - 1
    carry_over = 0
    result = []

    while pointer_a >= 0 or pointer_b >=0 or carry_over:

        num_a = int( a[pointer_a] ) if pointer_a >=0 else 0
        num_b = int( b[pointer_b] ) if pointer_b >=0 else 0

        print("pa",pointer_a,"b", pointer_b, "car",carry_over)
        total = num_a + num_b + carry_over
        append_dig = total % 2
        carry_over = total // 2

        result.append(str(append_dig))

        pointer_a -= 1
        pointer_b -= 1



        print("a", num_a, "b", num_b,"car",carry_over, "res", result)



    return "".join(reversed(result))

print( add_binary( "10101" , "1011" ) )
# print( add_binary( "11" , "1" ) )
# 1010 + 1011 = 10101