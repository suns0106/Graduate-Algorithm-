# BFS Iterative Solution

class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
         
class Solution(object):
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
