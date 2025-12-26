# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index_map = {inorder[i]: i for i in range(len(inorder))}
        def dfs(in_left, in_right):
            if in_left > in_right:
                return None
            
            val = postorder.pop()
            node = TreeNode(val)
            index = index_map[val]
            node.right = dfs(index+1, in_right)
            node.left = dfs(in_left, index-1)

            return node
        return dfs(0, len(inorder)-1)
        
        