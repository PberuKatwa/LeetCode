# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node
# down to the farthest leaf node.

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:

# Input: root = [1,null,2]
# Output: 2

from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self, root):
        self.root = root

    def build_tree(self, array:list):

        index = 0
        if self.root is None:
            self.root= TreeNode( array[0] )
            index = 1
        else:
            index = 0

        queue = deque([self.root])

        while index < len(array):
            parent = queue.popleft()

            left_val = array[index] if array[index] is not None else None
            right_val = array[index + 1] if array[index + 1] is not None else None

            if left_val:
                parent.left = TreeNode(left_val)
                queue.append(parent.left)

            if right_val:
                parent.right = TreeNode(right_val)
                queue.append(parent.right)

            index += 2
            
        return self
    
    def count_levels(self, node:TreeNode = None) -> int:

        if node is None:
            return 0

        # print ("weree heree", node.val)            
        left = self.count_levels(node.left)
        right = self.count_levels(node.right)

        value = left if left > right else right
        # print("value", value, "leff", left, "rigg", right) 

        return  1 + value
    
    def count_stack(self):

        if self.root is None:
            return 0

        count = 0

        node =  self.root
        # queue =  deque([node])
        queue =  deque([node])

        while queue:
            count += 1
            parent = queue.popleft()

            if parent.left:
                queue.append(parent.left)
            
            if parent.right:
                queue.append(parent.right)

        return count
    
    def count_all(self) -> int:

        if self.root is None:
            return 0
        
        max_length = 0
        node = self.root

        right = 0
        left = 0

        if node.left:
            left += self.count_levels(node.left)
        
        if node.right:
            right += self.count_levels(node.right)

            
        max_length = left if left > right else right

        return max_length + 1

    
binary_a = BinaryTree(None)
binary_a.build_tree( [3,9,20,None,None,15,7] )

binary_b = BinaryTree(None)
binary_b.build_tree([1,None,2])

print("p1_lvl", binary_a.count_all() )
# print("p1_lvl", binary_a.count_stack() )

print("p2_lvl", binary_b.count_all() )
# print("p2_SK", binary_b.count_stack() )