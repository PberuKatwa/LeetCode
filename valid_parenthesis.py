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
        "()":"None",
        "[]":"None",
        "{}":"None"
    }

    for char in string:

        print("character", char)

        if char == "(":
            parenthesis_dict["()"] = "opened"

        elif( char == ")" and parenthesis_dict["()"] == "opened" ):
            parenthesis_dict["()"] = True

        elif( char == ")" and parenthesis_dict["()"] != "opened" ):
            parenthesis_dict["()"] = "closed"

        elif(char == "["):
            parenthesis_dict["[]"] = "opened"

        elif( char == "]" and parenthesis_dict["[]"] == "opened" ):
            parenthesis_dict["[]"] = True

        elif( char == "]" and parenthesis_dict["[]"] != "opened" ):
            parenthesis_dict["[]"] = "closed"

        elif( char == "{"  ):
            parenthesis_dict["{}"] = "opened"

        elif( char == "}" and parenthesis_dict["{}"] == "opened"):
            parenthesis_dict["{}"] = True

        elif( char == "}" and parenthesis_dict["{}"] != "opened"):
            parenthesis_dict["{}"] = "closed"

        else:
            None


        print("parenthesis dict", parenthesis_dict)

        




    return parenthesis_dict


print(is_valid_parenthesis("()]{"))