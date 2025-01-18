# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curA = headA
        curB = headB
        chanceA, chanceB = 1, 1
        while curA and curB:
            if curA == curB:
                return curA
            curA = curA.next
            curB = curB.next
            if curA == None and chanceA == 1:
                curA = headB
                chanceA = 0
            if curB == None and chanceB == 1:
                curB = headA
                chanceB = 0
        return
            
            
            