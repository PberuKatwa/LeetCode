# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,3,2]

# Example 2:
# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
# Output: [4,2,6,5,7,1,3,9,8]

# Example 3:
# Input: root = []
# Output: []

# Example 4:
# Input: root = [1]

# Output: [1]

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self, root=None ):
        self.root = root

    def in_order(self):
        result = []

        def in_order_trans(node):

            if not node:
                return 

            in_order_trans(node.left)
            result.append(node.val)
            in_order_trans(node.right)

        in_order_trans(self.root)
        return result
    
    def pre_order_trasversal(self):
        result = []

        def pre_order(node):
            if not node:
                return
            
            result.append(node.val)
            pre_order(node.left)
            pre_order(node.right)

        pre_order(self.root)    
        return result
    
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

binary_tree = BinaryTree(root)



print("innnnn", binary_tree.in_order())
print("preee", binary_tree.pre_order_trasversal())


