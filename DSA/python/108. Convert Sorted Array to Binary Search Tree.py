# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def makeBST(start, end):
            if start == end:
                node = TreeNode(val=nums[start])
                return node
            elif start > end:
                return None
            else:
                mid = (start + end) // 2
                node = TreeNode(val=nums[mid])
                leftNode = makeBST(start, mid-1)
                rightNode = makeBST(mid+1, end)
                node.left = leftNode
                node.right = rightNode
                return node
        return makeBST(0, len(nums)-1)
        