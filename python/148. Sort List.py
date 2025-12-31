# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        
        return self.merge(left, right)


    
    def getMid(self, head):
        if head is None:
            return head
        count = 1
        cur = head
        while cur is not None:
            cur = cur.next
            count += 1
        
        mid_count = count // 2
        cur = head
        while mid_count != 1:
            cur = cur.next
            mid_count -= 1
        
        cur_next = cur.next
        cur.next = None

        return cur_next
    
    def merge(self, left, right):
        dummy = ListNode(0)
        tail = dummy

        while left or right:
            if left is None:
                tail.next = right
                break
            if right is None:
                tail.next = left
                break

            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next =right
                right = right.next
            tail = tail.next
        
        return dummy.next
        