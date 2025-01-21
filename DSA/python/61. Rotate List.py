# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None or k == 0:
            return head
        cur = head
        count = 1
        while cur.next != None:
            cur = cur.next
            count += 1
        k = k % count
        cur.next = head
        need_iterate_over = count - k
        while need_iterate_over > 1:
            head = head.next
            need_iterate_over -= 1
        cur = head
        head = head.next
        cur.next = None
        return head
        
