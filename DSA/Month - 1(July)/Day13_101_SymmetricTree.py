# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left = root.left
        right = root.right
        def isMirror(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            if left.val == right.val and right.val==left.val:
                return isMirror(left.left, right.right) and isMirror(left.right, right.left)
            else:
                return False
        return isMirror(left, right)
        


'''
Approach

The idea is to recursively check whether the left and right subtrees are mirror images of each other.

Create a helper function isMirror(left, right) that compares two nodes.

If both nodes are None, they are symmetric.
If one node is None and the other is not, they are not symmetric.
If the values of the two nodes are different, they are not symmetric.
Otherwise, recursively compare:
the left child of the left subtree with the right child of the right subtree.
the right child of the left subtree with the left child of the right subtree.

If both recursive comparisons return True, the tree is symmetric.

Algorithm
If the root is None, return True.
Define a helper function isMirror(left, right).
Inside the helper function:
If both nodes are None, return True.
If only one node is None, return False.
If the node values are different, return False.
Recursively check:
isMirror(left.left, right.right)
isMirror(left.right, right.left)
Return the logical AND of both recursive calls.
Call isMirror(root.left, root.right) and return its result.
Time Complexity
O(n)
Every node in the tree is visited exactly once.
Each node is compared only one time.

Therefore, the overall time complexity is:

O(n)
	​


where n is the number of nodes in the tree.

Space Complexity
O(h)

where h is the height of the tree.

This space is used by the recursive call stack.

Best case (balanced tree):
Height = log n
Space Complexity = O(log n)
Worst case (skewed tree):
Height = n
Space Complexity = O(n)

So the general space complexity is:

O(h)
	​


or O(n) in the worst case.

Summary
Aspect	Complexity
Approach	Recursive DFS (Mirror Comparison)
Operation	Compare left and right subtrees as mirror images
Time Complexity	O(n)
Space Complexity	O(h) (O(log n) for balanced tree, O(n) for skewed tree)

'''