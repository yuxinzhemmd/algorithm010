class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
            #1.回溯法
        def recur(num,col,pei,na,res):
            if num == n:
                ans[0] += 1
                return
            for i in range(n):
                if i in col or i-num in pei or num+i in na:
                    continue
                col.add(i)
                pei.add(i-num)
                na.add(num+i)
                res.append('.'*i+'Q'+'.'*(n-i-1))
                recur(num+1,col,pei,na,res)
                res.pop()
                col.remove(i)
                pei.remove(i-num)
                na.remove(i+num)
        col = set()
        pei = set()
        na = set()
        ans = [0]
        res = []
        recur(0,col,pei,na,res)
        return ans[0]