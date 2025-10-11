# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ls = []
        while head != None:
            ls.append(head.val)
            head = head.next
        if ls == ls[::-1]:
            return True
        return False