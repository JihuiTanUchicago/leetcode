# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        numList = []
        def getVal(root):
            if root == None:
                return
            numList.append(root.val)
            getVal(root.left)
            getVal(root.right)
        getVal(root)
        numList.sort()
        minDif = numList[1] - numList[0]
        for i in range(1, len(numList)-1):
            dif = numList[i+1] - numList[i]
            minDif = min(dif, minDif)
        return minDif

        
        