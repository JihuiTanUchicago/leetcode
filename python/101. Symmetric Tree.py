# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        def checkSymmetric(left, right):
            if left == None and right == None:
                return True
            if left == None or right == None:
                return False
            if left.val == right.val:
                return checkSymmetric(left.left,right.right) and checkSymmetric(left.right, right.left)
        return checkSymmetric(root.left, root.right) and checkSymmetric(root.right, root.left)
