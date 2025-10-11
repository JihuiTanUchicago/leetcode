# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def eval(root):
            if root.val == 0 or root.val == 1:
                return root.val
            else:
                left = eval(root.left)
                right = eval(root.right)
                if root.val == 3:
                    if left + right >= 2:
                        return 1
                    else:
                        return 0
                else:
                    if left + right >= 1:
                        return 1
                    else:
                        return 0
        final = eval(root)
        if final == 1:
            return True
        else:
            return False