# Given the root of a binary tree, check whether it is a mirror of itself
# (i.e., symmetric around its center).

# Example 1:
# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Example 2:
# Input: root = [1,2,2,null,3,null,3]
# Output: false

from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class BinaryTree:
    def __init__( self, root ):
        self.root = root

    def build_tree( self, array:list ):
        if len(array) < 1:
            return self
        
        index = None

        if self.root is None:
            self.root = TreeNode( array[0] )
            index = 1
        else:
            index = 0

        queue = deque( [self.root] )

        while index < len(array):
            parent = queue.popleft()

            left_val = array[index] if index < len(array) else None
            right_val = array[ index +1 ] if index + 1 < len(array) else None

            if left_val:
                parent.left = TreeNode(left_val)
                queue.append(parent.left)

            if right_val:
                parent.right =  TreeNode(right_val)
                queue.append(parent.right)

            index += 2

        return self
    
    def print_tree( self, node= None ):
        if node is None:
            node = self.root

        print(f'{node.val} ')

        if node.left:
            self.print_tree(node.left)
        
        if node.right:
            self.print_tree(node.right)

    def is_symetric(self, t1:TreeNode = None, t2:TreeNode = None ) -> bool:

        if t1 is None and t2 is None:
            if not self.root:
                return True

            return self.is_symetric(self.root.left,self.root.right)

        if not t1 and not t2:
            return True
        
        if t1 or t2 is None:
            return False
        
      
        return (
            t1.val == t2.val and
            self.is_symetric( t1.left, t2.right ) and
            self.is_symetric( t1.right, t2.left )
        )


binary_tree = BinaryTree(None)
binary_tree2 = BinaryTree(None)

binary_tree.build_tree([1,2,2,3,4,4,3])
binary_tree2.build_tree([1,2,2,None,3,None,3])


print( "tree 111", binary_tree.print_tree() )
print( "symmm 111", binary_tree.is_symetric() )

print( "tree 222", binary_tree2.print_tree() )
print( "symmm 222", binary_tree2.is_symetric() )





