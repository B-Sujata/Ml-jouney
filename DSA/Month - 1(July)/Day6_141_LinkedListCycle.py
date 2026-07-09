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

# Optimization to O(1) Space Complexity

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow = head
        fast= head
        
        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
            if slow==fast:
                return True
            
                
        return False
            

'''
Approach

The idea is to use two pointers to traverse the linked list at different speeds.

A slow pointer moves one node at a time.
A fast pointer moves two nodes at a time.

If the linked list contains a cycle, the fast pointer will eventually catch up to the slow pointer, causing both pointers to point to the same node.

If there is no cycle, the fast pointer will reach the end of the linked list (None), indicating that no cycle exists.

This approach avoids using any extra data structure, making it more space-efficient than the hash set approach.

Algorithm
Initialize two pointers, slow and fast, at the head of the linked list.
Traverse the linked list while both fast and fast.next are not None.
Move:
slow one step forward.
fast two steps forward.
After each move, check if slow and fast point to the same node.
If they do, return True because a cycle exists.
If the loop terminates because fast or fast.next becomes None, return False since no cycle exists.
Time Complexity

O(n)

The slow pointer visits each node at most once.
The fast pointer moves twice as fast, but together the total number of operations is still proportional to the number of nodes.
In the presence of a cycle, the fast pointer eventually catches the slow pointer after at most one traversal of the cycle.

Therefore,

Time Complexity = O(n)

where n is the number of nodes in the linked list.

Space Complexity

O(1)

Only two extra pointers are used:

slow
fast

No additional data structures such as arrays, hash maps, or hash sets are required.

Therefore,

Space Complexity = O(1)

💡 Why Floyd's Algorithm Works (Intuition)

Imagine two runners on a circular race track:

🐢 Tortoise (Slow Pointer) runs 1 step at a time.
🐇 Hare (Fast Pointer) runs 2 steps at a time.

If the track is circular (i.e., the linked list contains a cycle), the faster runner gains one step on the slower runner every move and must eventually catch up. When they meet, we know a cycle exists.

If the track is not circular (i.e., the linked list has no cycle), the faster runner eventually reaches the finish line (the None node), proving that no cycle is present.


'''