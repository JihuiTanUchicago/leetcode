"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None

        cur = head
        while cur != None:
            copy_prev = Node(x=cur.val)
            cur_next = cur.next
            cur.next = copy_prev
            copy_prev.next = cur_next
            cur = cur_next

        copy_head = head.next
        cur = head
        copy_cur = copy_head
        while copy_cur.next != None:
            if cur.random != None:
                copy_cur.random = cur.random.next
            cur = cur.next.next
            copy_cur.next = copy_cur.next.next
            copy_cur = copy_cur.next
        if cur.random != None:
            copy_cur.random = cur.random.next

        return copy_head
        
        
