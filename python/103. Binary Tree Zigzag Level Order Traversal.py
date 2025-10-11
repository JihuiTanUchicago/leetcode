# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        output = []
        cur_level = 0
        cur_list = []
        stack = [(root, 0)]

        while stack != []:
            node, level = stack.pop(0)
            if level > cur_level:
                cur_level = level
                cur_list = cur_list[::-1] if cur_level % 2 == 0 else cur_list
                output.append(cur_list)
                cur_list = []
            cur_list.append(node.val)
            ls = []
            if node.left != None:
                ls.append((node.left, level + 1))
            if node.right != None:
                ls.append((node.right, level + 1))
            stack += ls
        if cur_list != []:
            cur_list = cur_list[::-1] if cur_level % 2 != 0 else cur_list
            output.append(cur_list)
        return output