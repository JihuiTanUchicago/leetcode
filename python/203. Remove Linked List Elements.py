# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur = head
        while cur != None and cur.val == val:
            cur = cur.next
            head = cur
        if cur == None:
            return head
        while cur.next != None:
            while cur.next != None and cur.next.val == val:
                cur.next = cur.next.next
            cur = cur.next
            if cur == None:
                break
        return head

                



            