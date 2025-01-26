# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def returnSum(root):
            if root == None:
                return 0
            if root.val <= low:
                if root.val == low:
                    return root.val + returnSum(root.right)
                else:
                    return returnSum(root.right)
            if root.val >= high:
                if root.val == high:
                    return root.val + returnSum(root.left)
                else:
                    return returnSum(root.left)
            return root.val + returnSum(root.left) + returnSum(root.right)
        return returnSum(root)
        