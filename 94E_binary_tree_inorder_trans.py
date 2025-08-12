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

class BinaryTree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    
    def inorderTraversal(self):
        result = []    
        print("rooot starts", self.val)          

        def inorder(node):
            # print("in recurs", node.val)
            if not node:          # base case: empty subtree
                return
            inorder(node.left)   # 1) visit left subtree
            result.append(node.val)  # 2) visit the node itself
            # print("were at result", result)
            inorder(node.right)  # 3) visit right subtree

        inorder(self)            # start recursion from the root
        return result
    
root = BinaryTree(1)
root.right = BinaryTree(2)
root.right.left = BinaryTree(3)

print("hereeee", root.inorderTraversal())


