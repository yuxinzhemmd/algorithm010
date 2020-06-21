# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
    #1.递归
    #     res = []
    #     self.helper(root,res)
    #     return res

    # def helper(self,root,res):
    #     if root:
    #         res.append(root.val)
    #         self.helper(root.left,res)
    #         self.helper(root.right,res)
    #2.栈，迭代
        # stack = []
        # res = []
        # while root or stack:
        #     if root:
        #         a = root
        #         res.append(a.val)
        #         stack.append(a)
        #         root = root.left
        #     else:
        #         temp = stack.pop()
        #         root = temp.right
        # return res


        stack = []
        res = []
        while stack or root:
            if root:
                stack.append(root)
                res.append(root.val)
                root = root.left
            else:
                a = stack.pop()
                root = a.right
        return res