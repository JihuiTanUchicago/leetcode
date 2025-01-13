# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index_map = {}
        for i in range(len(inorder)):
            inorder_index_map[inorder[i]] = i
        
        preorder_index = 0
        def listToTree(left, right):
            nonlocal preorder_index
            if left > right:
                return None
            root = TreeNode(val=preorder[preorder_index])
            preorder_index += 1
            root.left = listToTree(left, inorder_index_map[root.val]-1)
            root.right = listToTree(inorder_index_map[root.val]+1, right)
            return root

        return listToTree(0, len(inorder)-1)
            
            

            
            
        