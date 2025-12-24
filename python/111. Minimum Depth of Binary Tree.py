# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        depth_cnt = 1
        current_level = [root]
        next_level = []
        while current_level != []:
            current_node = current_level.pop()
            if current_node.left == None and current_node.right == None:
                return depth_cnt
            else:
                if current_node.left != None:
                    next_level.append(current_node.left)
                if current_node.right != None:
                    next_level.append(current_node.right)

            if current_level == []:
                depth_cnt += 1
                current_level = next_level
                next_level = []
        
        return depth_cnt
        