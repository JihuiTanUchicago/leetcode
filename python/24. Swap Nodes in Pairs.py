# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return head
        h = head.next
        temp = head.next.next
        head.next.next = head
        head.next = temp
        head = h

        hook = h.next
        h = h.next.next
        while h and h.next:
            post_node = h.next.next
            first_node = h.next
            second_node = h
            pre_node = hook
            pre_node.next = first_node
            first_node.next = second_node
            second_node.next = post_node
            hook = second_node
            h = post_node

        return head

        