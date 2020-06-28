# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # if len(inorder) == 0:
        #     return
        # root = TreeNode(preorder[0])
        # mid = inorder.index(root.val)
        # root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
        # root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
        # return root
        if len(inorder) == 0:
            return
        t = TreeNode(preorder[0])
        mid = inorder.index(t.val)
        t.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
        t.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
        return t