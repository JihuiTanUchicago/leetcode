# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def passSum(root, summation):
            if root == None:
                return summation
            summation = int(str(summation) + str(root.val))
            if root.left == None and root.right == None:
                return summation
            if root.left == None:
                return passSum(root.right, summation)
            if root.right == None:
                return passSum(root.left, summation)
            return passSum(root.right, summation) + passSum(root.left, summation)
        return passSum(root, 0)