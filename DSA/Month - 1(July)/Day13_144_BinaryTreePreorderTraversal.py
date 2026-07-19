# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        if root is None:
            return []
        result.append(root.val)
        if root.left is not None:
            left =self.preorderTraversal(root.left)
            result.extend(left)
        if root.right is not None:
            right =self.preorderTraversal(root.right)
            result.extend(right)

        return result
        
'''
Approach

The idea is to perform a Preorder Depth First Search (DFS) traversal of the binary tree using recursion.

In preorder traversal, we visit the nodes in the following order:

Root → Left Subtree → Right Subtree

Starting from the root node, first add the current node's value to the result list. Then recursively traverse the left subtree to collect its preorder traversal, followed by the right subtree. Combine the results from both recursive calls with the current node's value to obtain the complete preorder traversal.

The recursion stops when it reaches a None node, which represents an empty subtree.

Algorithm
If the current node is None, return an empty list.
Create an empty list result.
Add the current node's value to result.
Recursively traverse the left subtree and append its traversal to result.
Recursively traverse the right subtree and append its traversal to result.
Return the result list.
Time Complexity
O(n)
Every node in the binary tree is visited exactly once.
Each node is processed only once by adding its value to the result list.

Therefore, for n nodes:

O(n)
	​

Space Complexity
O(h) (Recursion Stack)

where h is the height of the tree.

The recursive function calls are stored in the call stack.

Balanced Tree:
Height = log n
Space Complexity = O(log n)
Skewed Tree:
Height = n
Space Complexity = O(n)

Additionally, the output list stores all n node values, requiring O(n) space. Since the output list is required by the problem, it is typically not counted as auxiliary space.

Therefore, the auxiliary space complexity is:

O(h)
	​

Summary
Aspect	Complexity
Approach	Recursive DFS (Preorder Traversal)
Traversal Order	Root → Left → Right
Time Complexity	O(n)
Auxiliary Space Complexity	O(h)
Output Space	O(n)
💡 Interview Tip

For traversal problems, remember these three orders:

Preorder: Root → Left → Right
Inorder: Left → Root → Right
Postorder: Left → Right → Root

Notice that the recursive structure remains almost identical. The only thing that changes is when you process (append) the current node:

Before recursive calls → Preorder
Between recursive calls → Inorder
After recursive calls → Postorder



'''