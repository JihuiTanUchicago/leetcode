# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None:
            return head
        count = 1
        cur = head
        while cur.next != None:
            cur = cur.next
            count += 1
        front_n = count - n
        if front_n == 0: #first element to remove
            return head.next
        cur = head
        while front_n > 1:
            cur=cur.next
            front_n -= 1
        cur.next = cur.next.next
        return head
        