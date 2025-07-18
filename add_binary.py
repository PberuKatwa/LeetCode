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

def add_binary( a:str , b:str):

    pointer_a = len(a) 
    pointer_b = len(b)
    binary_string = ""
    range_val = pointer_b - 1
    carry_over = 0

    new_str = "0" * pointer_b

    if pointer_a > pointer_b:
        print("hereee")
        range_val = pointer_a - 1
        new_str = "0" * pointer_a

    print("range vall", range_val)
    print("new strr", new_str)
    for i in range( range_val , -1 , -1 ):

        num_a = int( a[i] ) or 0
        num_b = int( b[i] ) or 0
        current = 0

        if ( num_a == 0 ) and ( num_b == 0 ):                
            current = 0
        elif ( num_a == 1 ) and ( num_b == 1 ):
            carry_over = 1
            current = 0
            binary_string += "0"
            print("shoul carry")
            print(i,"int a b",num_a,num_b,"curr",current, "carr", carry_over,"binn",binary_string)

            continue
        else:
            current = 1

        if carry_over == 1 and current == 1 :
            print("shoul carry + carry")
            binary_string += "0"
            carry_over = 1

        elif carry_over == 0 and current == 1:
            binary_string +="1"
            carry_over = 0

        elif carry_over == 0 and current == 0:
            binary_string +="0"
            carry_over = 0

        elif carry_over == 1 and current == 0 :
            print("hereee")
            binary_string +="1"
            carry_over = 0

        print(i,"int a b",num_a,num_b,"curr",current, "carr", carry_over,"binn",binary_string)

    if carry_over == 1:
        binary_string +="1"






    return  ''.join(reversed(binary_string))

print( add_binary( "10101" , "1011" ) )
# print( add_binary( "11" , "1" ) )
# 1010 + 1011 = 10101