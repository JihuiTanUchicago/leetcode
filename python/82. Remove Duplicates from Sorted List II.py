# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        val = float('-inf')
        while cur != None:
            if head.val == val:
                head = head.next
                cur = head
            elif head.next != None and head.next.val == head.val:
                val = head.val
                head = head.next.next
                cur = head
            else:
                nxt = cur.next
                while nxt != None:
                    if nxt.val == val:
                        nxt = nxt.next
                    elif nxt.next != None and nxt.val == nxt.next.val:
                        val = nxt.val
                        nxt = nxt.next.next
                    else:
                        cur.next = nxt
                        break
                cur.next = nxt
                cur = cur.next
        return head