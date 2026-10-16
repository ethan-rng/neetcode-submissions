# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev, p1, p2 = None, l1, l2
        carryOver = 0

        while p1 and p2:
            temp = p1.val + p2.val + carryOver
            p1.val = temp % 10

            if temp >= 10:
                carryOver = 1
            else:
                carryOver = 0

            prev = p1
            p1 = p1.next
            p2 = p2.next

        # Either l1 has more digits than l2
        while p1:
            temp = p1.val + carryOver  
            p1.val = temp % 10

            if temp >= 10:
                carryOver = 1
            else:
                carryOver = 0    

            prev = p1
            p1 = p1.next


        # or l2 has more digits than l1
        if p2:
            p1 = ListNode()
            prev.next = p1

         # If l2 has more digits than l1
        if p2:
            prev.next = p2
            while p2:
                temp = p2.val + carryOver
                p2.val = temp % 10
                carryOver = temp // 10
                prev = p2
                p2 = p2.next



        # IF CARRY OVER IS STILL IN EFFECT
        if carryOver:
            prev.next = ListNode(1)



        return l1