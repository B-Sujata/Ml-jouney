# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        temp = head
        
        while temp is not None:
            if temp in visited:
                return True
            else:
                visited.add(temp)
                temp = temp.next
        return False
            
            
'''
LeetCode #141 — Linked List Cycle (Using Hash Set)
Approach

A linked list contains a cycle if we encounter the same node more than once while traversing it.

To detect this, we use a Hash Set to store the nodes that have already been visited.

While traversing the linked list:

If the current node is already present in the set, it means we have revisited the same node, indicating a cycle. Hence, return True.
Otherwise, add the current node to the set and move to the next node.
If we reach the end of the linked list (None), no node has been revisited, so the linked list does not contain a cycle.

This approach works because every node is a unique object, even if multiple nodes contain the same value.

Algorithm
Create an empty hash set named visited.
Initialize a pointer temp to the head of the linked list.
Traverse the linked list while temp is not None.
If temp is already present in the visited set:
Return True because a cycle exists.
Otherwise:
Add temp to the visited set.
Move temp to the next node.
If the traversal reaches None, return False because no cycle exists.
Time Complexity

O(n)

Each node is visited at most once before either:
reaching the end of the linked list, or
detecting a cycle.
Insertion and lookup operations in a hash set take O(1) time on average.

Therefore,

Time Complexity = O(n)

where n is the number of nodes in the linked list.

Space Complexity

O(n)

In the worst case, when there is no cycle, every node is stored in the hash set.

Example:

1 → 2 → 3 → 4 → 5 → None

The set contains:

{Node1, Node2, Node3, Node4, Node5}

Hence,

Space Complexity = O(n)

💡 Important Observation (Interview Point)

We do not store the values of the nodes in the hash set.

Instead, we store the node objects (references) themselves.

This is important because two different nodes can contain the same value.

For example:

5 → 7 → 5 → None

This linked list does not contain a cycle, even though the value 5 appears twice.

However,

      ┌──────────┐
      ↓          │
1 → 2 → 3 → 4 ───┘

contains a cycle because the traversal reaches the same node object again.

'''