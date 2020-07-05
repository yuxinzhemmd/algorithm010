class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        ans = 0
        # for i in g:
        #     for j in range(len(s)):
        #         if i <= s[j]:
        #             s.pop(j)
        #             ans += 1
        #             break
        # return ans
        i = 0
        j = 0

        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                ans += 1
                i += 1
                j += 1
            else:
                j += 1
        return ans