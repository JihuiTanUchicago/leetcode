"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return
        stack = [(root, 0)]
        level = 0
        while stack != []:
            node, cur_level = stack.pop(0)
            print(node.val, cur_level)

            if node.left != None:
                stack.append((node.left, cur_level+1))
            if node.right != None:
                stack.append((node.right, cur_level+1))

            if stack == [] or stack[0][1] > cur_level:
                level += 1
            else:
                node.next = stack[0][0]
        return root

            