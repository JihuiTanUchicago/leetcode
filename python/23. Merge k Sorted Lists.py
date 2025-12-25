# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        agg = []
        for ls in lists:
            if ls == None:
                continue
            cur = ls
            while cur != None:
                agg.append(cur.val)
                cur = cur.next
        agg.sort()
        head = ListNode(val=0, next=None)
        cur = head
        for i in range(len(agg)):
            new_node = ListNode(val=agg[i], next=None)
            cur.next = new_node
            cur = cur.next
        
        return head.next