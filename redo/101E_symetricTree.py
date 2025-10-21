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

    def build_tree(self,values:list):
        if not values:
            self.root = None


        if self.root is None:
            self.root = TreeNode(values[0])
            index = 1

        index = 0
        queue = [self.root]

        while index < len(values):

            parent = queue.pop()

            left_val = values[index] if index < len(values) else None
            right_val = values[index + 1] if index + 1 < len(values) else None

            if left_val is not None:
                parent.left = TreeNode(left_val)
                queue.append(parent.left)
                index += 1



            if right_val is not None:
                parent.right = TreeNode(right_val)
                queue.append(parent.right)
                index += 1

        return self

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

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

# binary_tree =  build_tree([1,2,2,3,4,4,3])

binary_2 = BinaryTree(None)
binary_2.build_tree([[1,2,2,3,4,4,3]])

# print("tree", print_preorder(binary_tree.root))

print("tree 2222", print_preorder( binary_2.root ) )