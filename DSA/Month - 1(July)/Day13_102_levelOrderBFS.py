# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = []
        result = []
        current_node = root
        queue.append(current_node)
        while len(queue)>0:
            level_size = len(queue)
            current_level = []
            for i in range(level_size):
                current_node = queue.pop(0)
                current_level.append(current_node.val)
                if current_node.left is not None:
                    queue.append(current_node.left)
                if current_node.right is not None:
                    queue.append(current_node.right)
            result.append(current_level)
            
            
        return result




'''
Note: Your implementation uses a Python list as a queue with pop(0), so the time complexity is different from the optimized deque solution.

Approach

The idea is to perform a Breadth First Search (BFS) traversal of the binary tree using a queue.

Initially, the root node is added to the queue. While the queue is not empty, the algorithm processes one level of the tree at a time. Before processing a level, the number of nodes currently in the queue is stored in level_size. This represents the total number of nodes present at the current level.

A loop runs level_size times to process every node of that level. Each node is removed from the front of the queue, its value is added to the current_level list, and its left and right children (if they exist) are added to the queue for processing in the next level.

After all nodes of the current level have been processed, the current_level list is appended to the final result. This process continues until the queue becomes empty.

Algorithm
If the root is None, return an empty list.
Create an empty queue and add the root node to it.
Create an empty list result to store the final answer.
While the queue is not empty:
Find the number of nodes in the current level using level_size = len(queue).
Create an empty list current_level.
Repeat level_size times:
Remove the front node from the queue.
Add its value to current_level.
If the left child exists, add it to the queue.
If the right child exists, add it to the queue.
Append current_level to result.
Return result.
Time Complexity
O(n²) (for this implementation)
Every node is visited exactly once.
However, the operation
queue.pop(0)

takes O(n) time because all the remaining elements in the list must shift one position to the left.

Since this operation is performed once for each node, the overall time complexity becomes:

O(n
2
)
	​


where n is the number of nodes in the tree.

Note: If a deque is used instead of a list, removing the front element with popleft() takes O(1) time, making the overall time complexity O(n).

Space Complexity
O(n)

The queue stores the nodes level by level.

In the worst case (such as a complete binary tree), the queue may contain approximately n/2 nodes at the last level.
The result list stores all n node values.

Therefore, the overall space complexity is:

O(n)
	​

Summary
Aspect	Complexity
Approach	Breadth First Search (BFS) using a Queue
Traversal Order	Level by Level
Time Complexity	O(n²) (using Python list with pop(0))
Optimized Time Complexity	O(n) (using deque.popleft())
Space Complexity	O(n)

'''