# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestDescendant(self, root):
        while root.right:
            root = root.right
        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.right == None:
                root = root.left
            elif root.left == None:
                root = root.right
            else:
                replace_val = self.largestDescendant(root.left).val
                root.val = replace_val
                root.left = self.deleteNode(root.left, replace_val)
        return root

        