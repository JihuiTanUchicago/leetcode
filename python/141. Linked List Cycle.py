# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        turtle = head
        rabbit = head
        while True:
            turtle = turtle.next
            rabbit = rabbit.next
            if rabbit == None:
                return False
            rabbit = rabbit.next
            if rabbit == None:
                return False
                
            if turtle == rabbit:
                return True
