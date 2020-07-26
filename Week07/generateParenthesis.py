class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
    #     res = []
    #     s = ''
    #     self._generate(0,0,n,res,s)
    #     return res
    # def _generate(self,left,right,n,res,s):
    #     #递归temple
    #     #1
    #     if left == n and right == n:
    #         return res.append(s)
    #     #2
    #     if left < n:
    #         self._generate(left+1, right, n, res, s+'(')
    #     if right < left:
    #         self._generate(left, right+1, n, res, s+')')
        def recur(left,right,n,res):
            if left == n and right == n:
                ans.append(res)
                return
            if left < n:
                recur(left+1,right,n,res+'(')
            if left > right:
                recur(left,right+1,n,res+')')
        ans = []
        res = ''
        recur(0,0,n,res)
        return ans