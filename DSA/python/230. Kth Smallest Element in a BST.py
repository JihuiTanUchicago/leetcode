# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ls = []
        def getNode(root):
            if root == None:
                return
            ls.append(root.val)
            getNode(root.left)
            getNode(root.right)
        getNode(root)
        ls.sort()
        return ls[k-1]