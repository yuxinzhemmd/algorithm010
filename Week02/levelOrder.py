class Solution(object):
    #1.迭代，使用队列进行层次遍历
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue =[root]
        res = []
        while queue:
            level = []
            for _ in range(len(queue)):
                a = queue.pop(0)
                level.append(a.val)
                queue.extend(a.children)
            res.append(level)
        return res