# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        turtle = head
        hare = head
        
        while hare != None:
            turtle = turtle.next
            hare = hare.next
            if hare == None:
                return False
            hare = hare.next

            if turtle == hare:
                return True
        return False

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         if head == None:
#             return False
#         turtle = head
#         rabbit = head
#         while True:
#             turtle = turtle.next
#             rabbit = rabbit.next
#             if rabbit == None:
#                 return False
#             rabbit = rabbit.next
#             if rabbit == None:
#                 return False
                
#             if turtle == rabbit:
#                 return True
