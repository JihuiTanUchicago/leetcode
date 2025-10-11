# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        if root == None:
            return output
        cur_level = 0
        level_ls = []
        stack = [(root,0)]
        while stack != []:
            node, level = stack.pop(0)
            if level > cur_level:
                cur_level = level
                output.append(level_ls)
                level_ls = [node.val]
            else:
                level_ls.append(node.val)
            if node.left != None:
                stack.append((node.left, level+1))
            if node.right != None:
                stack.append((node.right, level+1))

        if level_ls != []:
            output.append(level_ls)
            
        return output