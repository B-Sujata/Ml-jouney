# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        temp = head
        after = temp.next
        before = None

        while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return before
    
    '''
    LeetCode 206 - Reverse Linked List
Approach

We use three pointers to reverse the linked list without using any extra space.

temp (current) points to the node currently being processed.
before (previous) points to the already reversed portion of the linked list.
after (next) temporarily stores the next node before changing any links so that the remaining part of the list is not lost.

We traverse the linked list one node at a time. For every node, we first save the next node, then reverse the current node's next pointer to point to the previous node. After that, we move all three pointers one step forward.

Once the traversal is complete, the before pointer points to the head of the reversed linked list, which is returned.

Algorithm
Initialize before as None.
Initialize temp to point to the head of the linked list.
Traverse the linked list while temp is not None.
Store the next node in after using temp.next.
Reverse the current link by setting temp.next = before.
Move before to the current node.
Move temp to the next node stored in after.
Repeat until all nodes have been processed.
Return before, which points to the head of the reversed linked list.
Time Complexity

Let n be the number of nodes in the linked list.

Each node is visited exactly once, and every operation performed inside the loop takes constant time.

Therefore,

Time Complexity = O(n)

Space Complexity

Only three additional pointers are used:

before
temp
after

The amount of extra memory used does not depend on the size of the linked list.

Therefore,

Space Complexity = O(1)

Key Learning

This problem introduces the three-pointer technique, one of the most important concepts in linked lists.

Each pointer has a specific responsibility:

Pointer	Purpose
before	Points to the already reversed part of the linked list.
temp	Points to the current node being processed.
after	Temporarily stores the next node so the remaining list is not lost.
Why do we need the after pointer?

Suppose the linked list is:

1 → 2 → 3 → None

If we directly execute:

temp.next = before

without first saving temp.next, we lose the connection to the remaining nodes (2 → 3).

Therefore, before changing any pointers, we save the next node:

after = temp.next

This preserves access to the remaining part of the linked list.

Why do we return before instead of head?

Initially, head points to the first node of the original linked list.

As the algorithm progresses, only the links between nodes are reversed; the head variable itself never changes.

After processing all nodes:

temp becomes None.
before points to the last node of the original list, which is now the first node of the reversed list.

Hence, the correct return value is:

return before
🌟 Today's Biggest Takeaway

The most important lesson from this problem is:

Before modifying a pointer, always preserve any information you will need later.

This is why we first save:

after = temp.next

before changing:

temp.next = before

If we reverse the pointer without saving the next node, we lose access to the remaining linked list.

This idea of saving important information before modifying it is a recurring pattern in DSA and appears in many linked list, tree, and graph problems.
    
    
    '''

        
            
        

        