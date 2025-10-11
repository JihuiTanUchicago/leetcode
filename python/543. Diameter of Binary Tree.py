# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        def goDeep(root):
            nonlocal max_diameter
            if root == None:
                return 0
            if root.left != None:
                left_count = 1 + goDeep(root.left)
            else:
                left_count = 0
            if root.right != None:
                right_count = 1 + goDeep(root.right)
            else:
                right_count = 0
            max_diameter = max(max_diameter, left_count+right_count)
            return max(left_count, right_count)
        goDeep(root)
        return max_diameter
        