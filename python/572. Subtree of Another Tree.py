# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def checkDFS(root, subRoot, hasHeadChecked):
            print(f"checking root = {root.val if root!=None else -1} and subRoot = {subRoot.val if subRoot!=None else -1}")
            if root == None and subRoot == None:
                return True
            elif root == None and subRoot != None:
                return False
            elif root != None and subRoot == None:
                return False
            elif root.val == subRoot.val:
                check1 = checkDFS(root.left, subRoot.left, True) and checkDFS(root.right, subRoot.right, True)
                if check1 == True:
                    return True
                elif hasHeadChecked == True:
                    return False
                else:
                    return checkDFS(root.left, subRoot, False) or checkDFS(root.right, subRoot, False)
            else:
                if hasHeadChecked == False:
                    return checkDFS(root.left, subRoot, False) or checkDFS(root.right, subRoot, False)
                else:
                    return False
        return checkDFS(root, subRoot, False)