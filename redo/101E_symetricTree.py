# Given the root of a binary tree, check whether it is a mirror of itself
# (i.e., symmetric around its center).

# Example 1:
# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Example 2:
# Input: root = [1,2,2,null,3,null,3]
# Output: false
 
class BinaryTree:
    def __init__(self,root):
        self.root = root

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

# binary_tree =  TreeNode(1)
# binary_tree.left = TreeNode(2)
# binary_tree.right = TreeNode(2)
# binary_tree.left.left = TreeNode(3) 
# binary_tree.left.right = TreeNode(4) 
# binary_tree.right.left = TreeNode(4) 
# binary_tree.right.right = TreeNode(3) 

def build_tree(values:list) -> BinaryTree:
    if not values:
        BinaryTree(None)

    root = TreeNode( values[0] )
    index = 1

    queue = [root]

    while index < len(values):
        print("weree at start ....", values[index])

        parent = queue.pop()

        if index < len(values):
            left_val = values[index]

            print("lefft", left_val)
            if left_val is not None:
                print("found left valll", values[index])
                parent.left = TreeNode(left_val)
                queue.append(parent.left)
            else:
                print("no left val is found")
                parent.left = None

            index +=1

        if index < len(values):
            right_val = values[index]

            if right_val is not None:
                print("found rightt valllll", values[index])
                parent.right = TreeNode(right_val)
                queue.append(parent.right) 

            else:

                parent.right = None
                print("no righht vall is foundddd")

            index += 1

    return BinaryTree(root)

def print_preorder(node:TreeNode) ->str:
    if not node:
        return
    
    print(f'{node.val} ')
    print_preorder(node.left)
    print_preorder(node.right)

binary_tree =  build_tree([1,2,2,3,4,4,3])

print("tree", print_preorder(binary_tree.root))