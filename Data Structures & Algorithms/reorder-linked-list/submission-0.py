# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = deque([])

        s, f = head, head
        n = 0

        while f and f.next:
            s = s.next
            f = f.next.next
        
        curr = s.next
        s.next = None  # Break the list into two halves
        # ^ really fucking important otherwise u get 
        # 1 -> 4 -> 2 -> 3 -> 4 ...
        while curr:
            stack.append(curr)
            curr = curr.next

        #print(stack[0].val, stack)

        curr = head
        while stack:
            insertedNode = stack.pop()
            
            temp = curr.next
            curr.next = insertedNode
            insertedNode.next = temp

            curr = insertedNode.next
            
        
        