# Given the root of a binary tree, check whether it is a mirror of itself
# (i.e., symmetric around its center).

# Example 1:
# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Example 2:
# Input: root = [1,2,2,null,3,null,3]
# Output: false

from collections import deque

class BinaryTree:
    def __init__(self,root):
        self.root = root

    def build_tree(self,values:list):
        if not values:
            self.root = None

        index = None
        if self.root is None:
            self.root = TreeNode(values[0])
            index = 1
        else:
            index = 0

        queue =  deque( [self.root] )

        while index < len(values):

            parent = queue.popleft()

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
    
    def print_preorder(self, node=None):
        if node is None:
            node = self.root

        print(f'{node.val} ')
        if node.left:
            self.print_preorder(node.left)
        if node.right:
            self.print_preorder(node.right)

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

binary_2 = BinaryTree(None)
binary_2.build_tree([1,2,2,3,4,4,3])

print(  binary_2.print_preorder() )