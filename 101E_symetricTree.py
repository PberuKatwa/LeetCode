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

def create_tree(values):
    if not values:
        print("Empty input list. No tree created.")
        return BinaryTree(None)

    # Step 1: Create the root
    root = TreeNode(values[0])
    print(f"Created root node with value: {root.val}")

    # This queue holds parents waiting to get children
    queue = [root]
    index = 1  # index of the next value to assign

    # Step 2: Loop through the list and assign children
    while index < len(values):
        parent = queue.pop(0)  # take the oldest node waiting for children
        print(f"\n index {index},Parent node: {parent.val}, queeee 1st {queue}")

        if len(queue) > 0:
            f'\n current 1st que item {queue[0]}'

        # Assign left child
        if index < len(values):
            left_val = values[index]
            print(f"  Left child value from list: {left_val}")
            if left_val is not None:
                parent.left = TreeNode(left_val)
                queue.append(parent.left)
                print(f"  Created LEFT child {left_val} for parent {parent.val}")
            else:
                print(f"  No LEFT child for parent {parent.val}")
            index += 1

        # Assign right child
        if index < len(values):
            right_val = values[index]
            print(f"  Right child value from list: {right_val}")
            if right_val is not None:
                parent.right = TreeNode(right_val)
                queue.append(parent.right)
                print(f"  Created RIGHT child {right_val} for parent {parent.val}")
            else:
                print(f"  No RIGHT child for parent {parent.val}")
            index += 1

        print(f"\ncurrent queue", "1st",queue[0].val, "2nd", queue[1].val)

    return BinaryTree(root)


# Example run
new_tree = create_tree([1, 2, 2, 3, 4, 4, 3])

nw_rt = new_tree.root

print( "trrrrr",new_tree, "rrr", nw_rt.val, "leff", nw_rt.left.val, "right", nw_rt.right.val,"l2 left", nw_rt.left.left.val, " r2 ", nw_rt.left.right.val )
        
