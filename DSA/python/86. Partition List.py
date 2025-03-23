# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head == None:
            return None
        cur = ListNode(val=float('-inf'), next = head)
        head = cur
        while cur.next != None:
            if cur.next.val < x:
                cur = cur.next
            else:
                curGreater = cur
                while curGreater.next != None:
                    while curGreater.next != None and curGreater.next.val >= x:
                        curGreater = curGreater.next
                    if curGreater == None or curGreater.next == None:
                        break
                    temp = cur.next
                    cur.next = curGreater.next
                    curGreater.next = curGreater.next.next
                    cur.next.next = temp
                    cur = cur.next
                break
        return head.next

            