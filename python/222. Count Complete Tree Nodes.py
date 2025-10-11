# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countDepth(self, root):
        d = 0
        while root:
            d += 1
            root = root.left
        return d
    
    def getLeafByIndex(self, index, root, d):
        left, right = 0, 2**(d-1)-1
        for _ in range(d-1):
            mid = left + (right-left) // 2
            if index <= mid:
                root = root.left
                right = mid
            else:
                root = root.right
                left = mid+1
        return root is not None

    def countNodes(self, root: Optional[TreeNode]) -> int:
        d = self.countDepth(root)
        sums = 0
        for i in range(d-1):
            sums += 2 ** i
        left, right = 0, 2**(d-1) - 1
        while left <= right:
            mid = left + (right-left)//2
            print(mid)
            leaf_exists = self.getLeafByIndex(mid, root, d)
            print(leaf_exists)
            if leaf_exists:
                left = mid + 1
            else:
                right = mid - 1
        sums += left
        return sums

