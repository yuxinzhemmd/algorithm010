class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #1.排序再比较,O(nlogn)
        if(len(s) != len(t)):
            return False
        if sorted(list(s)) == sorted(list(t)):
            return True
        else: 
            return False
        #2.用一个dict记录出现的次数,O(n)
        # if(len(s) != len(t)):
        #     return False
        # count = {}
        # for i in s:
        #     if i not in count:
        #         count[i] += 1
        #     else:
        #         count[i] = 1
        # for j in t:
        #     if j in count:
        #         count[j] -= 1
        #     else:
        #         count[j] = 1
        # for k in count.values():
        #     if k != 0:
        #         return False
        # return True
        #3.别人的代码，ord()返回ASCLL码
        # return abs(sum([ord(x)**0.5 for x in s])-sum([ord(y)**0.5 for y in t]))<1e-5