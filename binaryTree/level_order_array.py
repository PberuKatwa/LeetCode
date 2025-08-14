# Problem:
# Given the inorder traversal of a binary tree, reconstruct all possible binary trees that could produce this traversal.
# You must return a list of root nodes representing each unique tree.

# Example:
# Input: inorder = [1, 2, 2, 3, 4, 4, 3]
# Output: (multiple trees possible)

# Possible interpretations:
# A balanced binary tree.
# A skewed tree (left-heavy or right-heavy).
# Trees with duplicate value arrangements that still yield the same inorder.

# Constraints:
# 1 <= len(inorder) <= 10
# Tree node values can be duplicates.
# Return structure should allow traversal verification.

class BinaryTree:
    def __init__(self,root):
        self.root = root

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def create_balanced_tree(input:list) -> BinaryTree:
    n = len(input)
    index = 1
    root = TreeNode( input[0] )
    queue = [ root ]

    while index < n :

        parent  = queue.pop(0)

        if index < n :
            left_val = input[index]

            if left_val is not None:
                parent.left = TreeNode ( left_val )
                queue.append(parent.left)
            index += 1
        
        if index < n :
            right_val = input[index]

            if right_val is not None:
                parent.right = TreeNode ( right_val )
                queue.append(parent.right)
            index += 1

    binary_tree = BinaryTree(root)
    return binary_tree

def create_skewed_tree(input:list,skew:str) -> BinaryTree:

    n =  len(input)
    index = 1
    root = TreeNode(input[0])
    stack = [ root ]


    while index < n:

        parent = stack.pop()
        print(f"\n  parrentt {parent.val}, skew: {skew.upper()}")

        if skew.upper() == "LEFT":

            val = input[index]
            if val is not None:
                print(f"\n lefttt skew: val: {val}")

                parent.left = TreeNode( val )
                stack.append( parent.left )
            index += 1
        
        elif skew.upper() == "RIGHT":

            val = input[index]
            if val is not None:
                print(f"\n right skew: val: {val}")

                parent.right = TreeNode( val )
                stack.append( parent.right )
            index += 1

    tree = BinaryTree(root)
    return tree

def level_order(node:TreeNode) -> list:
    if not node:
        return []
    
    output = []
    queue = [ node ]

    while queue:
        current = queue.pop(0)

        output.append(current.val)
        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    return output

balanced_tree = create_balanced_tree([1, 2, 2, 3, 4, 4, 3])
skewed_tree = create_skewed_tree([1, 2, 2, 3, 4, 4, 3],"left")

# print(f'/n order ::: {level_order(balanced_tree.root)}')
print(f'\n tree ::: {level_order(skewed_tree.root)}')