# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        stack2 = []

        cur_l1, cur_l2 = l1, l2
        while cur_l1 != None:
            stack1.append(cur_l1.val)
            cur_l1 = cur_l1.next
        while cur_l2 != None:
            stack2.append(cur_l2.val)
            cur_l2 = cur_l2.next
        
        if len(stack1) < len(stack2):
            stack1, stack2 = stack2, stack1
        for i in range(len(stack1)):
            if i < len(stack2):
                stack1[-i-1] += stack2[-i-1]
            if stack1[-i-1] >= 10:
                stack1[-i-1] -= 10
                if -i-2 < -len(stack1):
                    stack1 = [1] + stack1
                else:
                    stack1[-i-2] += 1
            
        

        if len(stack1) > 0:
            head = ListNode(val=stack1[0], next = None)
            cur = head
            for i in range(1, len(stack1)):
                cur_node = ListNode(val=stack1[i], next=None)
                cur.next = cur_node
                cur = cur.next

        return head