# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
    #1.递归法
        return self.recur(root,p,q)
    def recur(self,root,p,q):   
        #1.terminator
        if root == None or root == p or root == q:
            return root

        #2.process logic
        l = self.recur(root.left,p,q)
        r = self.recur(root.right,p,q)
        if not l:    return r
        if not r:   return l
        return root