# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if right <= left:
            return head
        prehead = ListNode(val=0)
        prehead.next = head
        cur = prehead
        count = 1
        while left - count >= 1:
            cur = cur.next
            count += 1
        left_part = cur
        cur = cur.next
        right_part = cur
        prev = cur
        cur = cur.next
        nxt = None
        while count < right:
            count += 1
            nxt = cur.next
            cur.next = prev
            prev = cur
            if count != right:
                cur = nxt
        left_part.next = cur
        right_part.next = nxt
        return prehead.next

        