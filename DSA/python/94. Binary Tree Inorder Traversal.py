# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ls = []
        def goInorder(root):
            if root == None:
                return
            goInorder(root.left)
            ls.append(root.val)
            goInorder(root.right)
        goInorder(root)
        return ls