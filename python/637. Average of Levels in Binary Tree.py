# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        arr = [[0,0]]
        def updateAverage(root, level):
            if root == None:
                return
            if len(arr) <= level:
                arr.append([0,0])
            arr[level][0] += 1
            arr[level][1] += root.val
            updateAverage(root.left, level+1)
            updateAverage(root.right, level+1)
        updateAverage(root, 0)
        avg_arr = [(lambda x: x[1]/x[0])(x) for x in arr]
        print(avg_arr)
        return avg_arr


        