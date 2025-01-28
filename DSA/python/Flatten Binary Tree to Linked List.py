# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return None
        def skrrah_pu_pu_brr_boom_boom(big_shaq): #lol
            two_plus_two_is_four = big_shaq.right
            if big_shaq.left != None:
                quick_math = skrrah_pu_pu_brr_boom_boom(big_shaq.left)
                big_shaq.right = quick_math
                big_shaq.left = None
                while quick_math.right != None:
                    quick_math = quick_math.right
                quick_math.right = two_plus_two_is_four
            if two_plus_two_is_four != None:
                skrrah_pu_pu_brr_boom_boom(two_plus_two_is_four)
            return big_shaq
        skrrah_pu_pu_brr_boom_boom(big_shaq = root)
