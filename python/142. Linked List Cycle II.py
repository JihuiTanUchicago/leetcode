# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        turtle = head
        hare = head

        while hare != None:
            turtle = turtle.next
            hare = hare.next
            if hare is None:
                return None
            hare = hare.next
            if hare is None:
                return None

            if turtle == hare:
                hare = head
                break
        

        while turtle != hare:
            turtle = turtle.next
            hare = hare.next
            if turtle == hare:
                return turtle
        
        return turtle
