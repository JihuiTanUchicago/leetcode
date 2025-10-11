# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        smallest = 'z' * 8501
        def dfs(cur_string, depth, root):
            nonlocal smallest
            if root == None:
                return
            cur_string = chr(root.val + 97) + cur_string
            if root.left == None and root.right == None: #leaf
                smallest = min(smallest, cur_string)
                return
            if root.left != None:
                dfs(cur_string, depth+1, root.left)
            if root.right != None:
                dfs(cur_string, depth+1, root.right)
        dfs('', 0, root)
        return smallest
                    
            

