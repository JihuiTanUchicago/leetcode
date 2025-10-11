# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or head.next == None:
            return head
        total_count = 0
        temp = head
        while temp != None:
            total_count += 1
            temp = temp.next

        count = k
        pre_head = ListNode(val=float('inf'))
        pre_head.next = head
        cur_pre_head = pre_head
        cur_head = pre_head.next
        track = pre_head.next
        cur_node = cur_head.next
        while total_count >= k:
            if count == 1:
                cur_head.next = cur_node
                cur_pre_head.next = track
                cur_pre_head = cur_head
                cur_head = cur_node
                track = cur_node
                if cur_node == None:
                    break
                cur_node = cur_node.next
                count = k
                total_count -= k
                continue
            nxt = cur_node.next
            cur_node.next = track
            track = cur_node
            cur_node = nxt
            count -= 1
        return pre_head.next
