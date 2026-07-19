

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None :
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        depth = 1 + max(left_depth, right_depth)

        return depth
    
    '''
    Approach

The idea is to use Depth First Search (DFS) with recursion to calculate the maximum depth of the binary tree.

Starting from the root node, recursively calculate the depth of the left subtree and the depth of the right subtree. Since the maximum depth of a tree is determined by its deepest subtree, take the maximum of the two depths and add 1 to count the current node.

The recursion stops when it reaches a None node, which represents an empty tree and has a depth of 0.

Algorithm
If the current node is None, return 0.
Recursively calculate the maximum depth of the left subtree.
Recursively calculate the maximum depth of the right subtree.
Find the larger of the two depths.
Add 1 to include the current node.
Return the calculated depth.
Time Complexity
O(n)
Every node in the tree is visited exactly once.
Each visit performs only constant-time operations:
Two recursive calls
One max() operation
One addition

Therefore, if there are n nodes, the total time complexity is:

O(n)
	​

Space Complexity
O(h)

where h is the height of the tree.

This space is used by the recursion call stack.

Best Case (Balanced Tree):
Height = log n
Space Complexity = O(log n)
Worst Case (Skewed Tree):
Height = n
Space Complexity = O(n)

Therefore, the general space complexity is:

O(h)
	​


where h is the height of the tree.

Summary
Aspect	Complexity
Approach	Recursive DFS (Post-order Traversal)
Time Complexity	O(n)
Space Complexity	O(h) (O(log n) for balanced tree, O(n) for skewed tree)
    
    
    '''
        