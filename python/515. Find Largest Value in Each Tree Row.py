# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        if root == None:
            return output
        node_list = [(root,0)]
        val_list = [root.val]
        cur_depth = 0
        while node_list != []:
            node, depth = node_list.pop(0)
            if depth > cur_depth:
                output.append(max(val_list))
                val_list = []
                cur_depth = depth
            val_list.append(node.val)
            if node.left != None:
                node_list.append((node.left, depth+1))
            if node.right != None:
                node_list.append((node.right, depth+1))
        if val_list != []:
            output.append(max(val_list))
        
        return output

#