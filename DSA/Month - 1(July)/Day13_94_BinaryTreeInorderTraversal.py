# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        if root.left is not None:
            left = self.inorderTraversal(root.left)
            result.extend(left)
        result.append(root.val)
        if root.right is not None:
            right = self.inorderTraversal(root.right)
            result.extend(right)
        return result

        
'''
Approach

The idea is to perform an Inorder Depth First Search (DFS) traversal of the binary tree using recursion.

In inorder traversal, the nodes are visited in the following order:

Left Subtree → Root → Right Subtree

Starting from the root node, recursively traverse the left subtree and collect its inorder traversal. After visiting the left subtree, add the current node's value to the result list. Finally, recursively traverse the right subtree and append its traversal to the result list.

The recursion stops when it reaches a None node, which represents an empty subtree.

Algorithm
If the current node is None, return an empty list.
Create an empty list result.
Recursively traverse the left subtree and store its inorder traversal.
Append the left subtree traversal to result.
Add the current node's value to result.
Recursively traverse the right subtree and store its inorder traversal.
Append the right subtree traversal to result.
Return the result list.
Time Complexity
O(n)
Every node in the binary tree is visited exactly once.
Each node is added to the result list only once.

Therefore, the total time complexity is:

O(n)
	​


where n is the number of nodes in the tree.

Space Complexity
O(h) (Auxiliary Space)

where h is the height of the tree.

The recursive function calls are stored in the call stack.

Balanced Tree:
Height = O(log n)
Space Complexity = O(log n)
Skewed Tree:
Height = O(n)
Space Complexity = O(n)

The returned result list stores all n node values, which requires O(n) space. Since this is the required output of the problem, it is generally not considered auxiliary space.

Therefore, the auxiliary space complexity is:

O(h)
	​

Summary
Aspect	Complexity
Approach	Recursive DFS (Inorder Traversal)
Traversal Order	Left → Root → Right
Time Complexity	O(n)
Auxiliary Space Complexity	O(h)
Output Space	O(n)
💡 Pattern to Remember

All three recursive traversals have the same recursive structure. The only difference is where you process the current node:

Traversal	Order
Preorder	Root → Left → Right
Inorder	Left → Root → Right
Postorder	Left → Right → Root

This single change in the position of result.append(root.val) changes the traversal type. Once you understand this pattern, all three traversal problems become straightforward.


'''