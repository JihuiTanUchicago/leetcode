# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, range):
            if root == None:
                return True
            if root.left == None and root.right == None:
                return range[0] < root.val < range[1]
            if root.val <= range[0] or root.val >= range[1]:
                return False
            return dfs(root.left, [range[0], min(root.val, range[1])]) and dfs(root.right, [max(root.val, range[0]), range[1]])
        return dfs(root, [float('-inf'), float('inf')])

            