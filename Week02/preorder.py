"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        #1.递归
    #     res = []
    #     self.helper(root,res)
    #     return res

    # def helper(self,root,res):
    #     if root:
    #         res.append(root.val)
    #         for child in root.children:
    #             self.helper(child,res)
            
        #2.迭代
        if root is None:
            return []
        stack = [root]
        res = []
        while stack:
            root = stack.pop()
            res.append(root.val)
            stack.extend(root.children[::-1])
        return res