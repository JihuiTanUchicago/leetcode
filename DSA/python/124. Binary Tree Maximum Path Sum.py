class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maximum = float('-inf')
        def getMax(root):
            nonlocal maximum
            if root == None:
                return 0
            leftMax = getMax(root.left)
            rightMax = getMax(root.right)
            maximum = max(root.val, root.val + leftMax + rightMax, maximum)
            return max(0, root.val, root.val + max(leftMax, rightMax))
        getMax(root)
        return maximum