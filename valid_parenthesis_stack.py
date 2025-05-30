# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:
# Input: s = "()"
# Output: true
# Example 2:
# Input: s = "()[]{}"
# Output: true
# Example 3:
# Input: s = "(]"
# Output: false
# Example 4:
# Input: s = "([])"
# Output: true

def is_valid_parenthesis(string:str):
    length = len(string)
    n = length - 1
    i = 0
    parenthesis_dict = {
        ")":"(",
        "]":"[",
        "}":"{"
    }

    stack = []
    elem = None
    result = None

    for char in string:
        i = i + 1
        print("loop counter", i)
        print("charrr", char)
        print("stack ....", stack)

        if char in parenthesis_dict:
            
            if len(stack) != 0 :
               elem = stack.pop()
               if parenthesis_dict[char] != elem:
                    return False
               else:                  
                   print("foundddd")
            else:
                '#' 

            # elem = stack.pop() if stack else "#"
            print("elem", elem)

        else:
            stack.append(char)
            print("apenddd",stack)

    if( len(stack) == 0 ):
        result = True
    else:
        result = False

    return result


print(is_valid_parenthesis("({})"))