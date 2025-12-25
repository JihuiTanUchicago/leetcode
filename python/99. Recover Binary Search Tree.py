# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(root):
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []
        inorder_list = inorder(root)
        print(inorder_list)
        smaller_val, larger_val = None, None
        for i in range(len(inorder_list)):
            if i == 0:
                if inorder_list[i] > inorder_list[i+1]:
                    larger_val = inorder_list[i]
            elif i == len(inorder_list) - 1:
                if inorder_list[i] < inorder_list[i-1]:
                    smaller_val = inorder_list[i]
            elif inorder_list[i] < inorder_list[i-1] and inorder_list[i] < inorder_list[i+1]:
                smaller_val = inorder_list[i]
            elif inorder_list[i] > inorder_list[i-1] and inorder_list[i] > inorder_list[i+1]:
                if larger_val == None:
                    larger_val = inorder_list[i]
        print(smaller_val, larger_val)
        
        def change_val(root):
            if root == None:
                return
            elif root.val == smaller_val:
                root.val = larger_val
            elif root.val == larger_val:
                root.val = smaller_val
            change_val(root.left)
            change_val(root.right)
        change_val(root)


            

        