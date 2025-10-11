# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        prev = None
        curr = head
        nxt = head.next
        while curr != None:
            curr.next = prev
            prev = curr
            if nxt != None:
                curr = nxt
                nxt = curr.next
            else:
                return curr