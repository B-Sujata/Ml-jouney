# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        queue = []
        
        current_node = root
        queue.append(current_node)
        while len(queue)>0:
            current_node = queue.pop(0)
            current_node.left, current_node.right = current_node.right, current_node.left
            
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return current_node


'''
Approach

The idea is to perform a Breadth First Search (BFS) traversal of the binary tree using a queue.

Start by adding the root node to the queue. While the queue is not empty, remove the front node and swap its left and right child pointers. After swapping, if the left or right child exists, add them to the queue so they can also be inverted.

This process continues until every node in the tree has been visited and its children have been swapped. Since the tree is modified in place, the root of the modified tree is returned.

Algorithm
If the root is None, return None.
Create an empty queue and add the root node to it.
While the queue is not empty:
Remove the front node from the queue.
Swap its left and right child pointers.
If the left child exists, add it to the queue.
If the right child exists, add it to the queue.
Return the root of the inverted tree.
Time Complexity
O(n²) (for this implementation)
Every node in the tree is visited exactly once.
However, the operation
queue.pop(0)

takes O(n) time because all remaining elements in the list must shift one position to the left.

Since this operation is performed once for each node, the overall time complexity becomes:

O(n
2
)
	​


where n is the number of nodes in the tree.

Optimized Version: If a deque is used instead of a list, popleft() removes the front element in O(1) time, reducing the overall time complexity to:

O(n)
	​

Space Complexity
O(n)

The queue stores the nodes level by level.

In the worst case (for a complete binary tree), the queue may contain approximately n/2 nodes at the last level.

Therefore, the auxiliary space required by the queue is:

O(n)
	​


The tree is inverted in place, so no additional tree or data structure proportional to the number of nodes is created.

Summary
Aspect	Complexity
Approach	Breadth First Search (BFS) using a Queue
Operation	Swap the left and right child of every node
Time Complexity	O(n²) (using Python list with pop(0))
Optimized Time Complexity	O(n) (using deque.popleft())
Space Complexity	O(n)

'''