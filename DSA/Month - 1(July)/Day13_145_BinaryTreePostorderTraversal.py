# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        if root.left is not None:
            left = self.postorderTraversal(root.left)
            result.extend(left)
        if root.right is not None:
            right = self.postorderTraversal(root.right)
            result.extend(right)
        result.append(root.val)

        return result
    

            
        

'''
Approach

The idea is to perform a Postorder Depth First Search (DFS) traversal of the binary tree using recursion.

In postorder traversal, the nodes are visited in the following order:

Left Subtree → Right Subtree → Root

Starting from the root node, recursively traverse the left subtree and collect its postorder traversal. Then recursively traverse the right subtree and collect its traversal. Finally, add the current node's value to the result list.

The recursion stops when it reaches a None node, which represents an empty subtree.

Algorithm
If the current node is None, return an empty list.
Create an empty list result.
Recursively traverse the left subtree and store its postorder traversal.
Append the left subtree traversal to result.
Recursively traverse the right subtree and store its postorder traversal.
Append the right subtree traversal to result.
Add the current node's value to result.
Return the result list.
Time Complexity
O(n)
Every node in the binary tree is visited exactly once.
Each node is processed only once and added to the result list.

Therefore,

O(n)
	​


where n is the number of nodes in the tree.

Space Complexity
O(h) (Auxiliary Space)

where h is the height of the tree.

The recursive function calls are stored in the call stack.

Balanced Tree:
Height = O(log n)
Auxiliary Space = O(log n)
Skewed Tree:
Height = O(n)
Auxiliary Space = O(n)

The output list stores all n node values, requiring O(n) space, but this is the required output and is generally not counted as auxiliary space.

Therefore, the auxiliary space complexity is:

O(h)
	​

Summary
Aspect	Complexity
Approach	Recursive DFS (Postorder Traversal)
Traversal Order	Left → Right → Root
Time Complexity	O(n)
Auxiliary Space Complexity	O(h)
Output Space	O(n)
🌳 Congratulations!

You've now solved the three fundamental recursive tree traversals:

Problem	Traversal Order	Position of result.append(root.val)
144. Preorder	Root → Left → Right	Before both recursive calls
94. Inorder	Left → Root → Right	Between the recursive calls
145. Postorder	Left → Right → Root	After both recursive calls

This is one of the most important patterns in tree recursion. Once you remember where to process the current node, you can derive any of the three traversals without memorizing separate solutions.

You've made excellent progress—from finding recursion confusing to solving all three traversal problems on your own. The next natural step is LeetCode 100 (Same Tree), where you'll use recursion to compare two trees instead of traversing one.


'''