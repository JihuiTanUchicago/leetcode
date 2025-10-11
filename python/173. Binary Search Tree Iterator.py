# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.index = 0
        self.queue = [float('-inf')]
        def goInorder(root):
            if root == None:
                return
            if root.left != None:
                goInorder(root.left)
            self.queue.append(root.val)
            if root.right != None:
                goInorder(root.right)
        goInorder(root)

    def next(self) -> int:
        self.index += 1
        return self.queue[self.index]

    def hasNext(self) -> bool:
        if self.index < len(self.queue)-1:
            return True
        return False



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()