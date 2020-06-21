# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #1.递归，
    #     res = []
    #     self.helper(root,res)
    #     return res

    # def helper(self,root,res):
    #     if root:
    #         self.helper(root.left,res)
    #         res.append(root.val)
    #         self.helper(root.right,res)  
    #2.栈,O(n)
        stack = []
        res = []
        while stack or root:
            if root:
                a = root
                stack.append(a)
                root = root.left
            else:
                temp = stack.pop()
                res.append(temp.val)
                root = temp.right
        return res