class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #1.DP hashmap
        """
        重复子问题：subproblem(i)=subproblem(i-1)+1
        dp数组：len(s)
        递推方程：f(i) = f(i-1)+1
        """
        pp, p = 1, int(s[0] != '0')
        for i in range(1, len(s)):
            pp, p = p, pp * (9 < int(s[i-1:i+1]) <= 26) + p * (int(s[i]) > 0)
        return p