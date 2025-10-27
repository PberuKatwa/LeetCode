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
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root ):
        self.root = root

    def build_tree(self, array:list):

        index = None

        if self.root is None:
            self.root = TreeNode(array[0])
            index = 1
        else:
            index = 0

        queue = deque( [self.root] )

        while index < len(array):
            parent = queue.popleft()

            left_val = array[index] if array[index] else None
            right_val = array[index + 1 ] if array[index + 1] else None

            if left_val:
                parent.left = TreeNode( left_val )
                queue.append(parent.left)

            if right_val:
                parent.right = TreeNode(right_val)
                queue.append(parent.right)

            index += 2
                
        return self.root
    
    def print_tree(self, node = None ):

        if not node:
            if self.root is None:
                print(f'Noneeeee')

            node = self.root

        print(f'{node.val} ')

        if node.left:
            self.print_tree(node.left)

        if node.right:
            self.print_tree(node.right)

    def maximum_depth(self, array:list ) -> int:
        length = 0

        index = None
        if self.root is None:
            self.root = TreeNode(array[0])
            index = 1
        else:
            index = 0


        queue = deque([self.root])

        if index < len(array):
            parent =  queue.popleft()

            left_val = array[index] if array[index] else None
            right_val = array[index + 1] if array[index + 1 ] else None

            if left_val:
                parent.left= TreeNode(left_val)
                queue.append(parent.left)

            if right_val:
                parent.right = TreeNode(right_val)
                queue.append(parent.right)

            index += 2

            if right_val or left_val:
                length +=1

        return length


    def count_node( self, node:TreeNode = None ) -> int:

        
        if node is None:
            return 0
        
        print("werreee heree", node.val)
        
        left = self.count_node(node.left)
        right = self.count_node(node.right)
        
        return 1 + left + right
    
    def count_node2( self ) -> int:
        if self.root is None:
            return 0

        count = 0

        queue = deque([self.root])
        left = 0
        right = 0
        while queue:
            parent = queue.popleft()

            print("BGGG wereee here", parent.val)
            if parent.left:
                print("LLLL werrre herre", parent.left.val)
                left += 1
                queue.append(parent.left)

            if parent.right:
                print("RRRR werrre herre", parent.right.val)

                right += 1
                queue.append(parent.right)

        print("leftt", left, "rightt", right)
        count = left if left > right else right

        return count

    def max_2(self, node:TreeNode = None) -> int:
        max_length = 0

        print("weree at beginning", node)
        if ( node is None ):
            if self.root is None:
                return max_length
            
            return self.max_2( self.root)
        
        left_length = 0
        right_length = 0

        if node.left:
            nw_length = self.count_node2(node.left)
            print("nwww", nw_length)
            left_length += nw_length 
            print("NODE_1 weree hereee at node", left_length)
        
        if node.left:
            nw_length = self.count_node2(node.right)
            right_length += nw_length 
            print("NODE_22 weree hereee at node", right_length)

        max_length = left_length if left_length > right_length else right_length

        return max_length


binary_a = BinaryTree(None)
binary_a.build_tree([3,9,20,"null","null",15,7])

binary_b = BinaryTree(None)
# binary_b.build_tree([3,9,20,"null","null",15,7])
binary_b.build_tree([ 3, 9, 20, None, None, 15, 7 ])

# print( "tre 1", binary_a.print_tree() )

# print("tre 2", binary_b.print_tree() )
# print("depth", binary_b.max_2() )

print("depth", binary_b.count_node2() )