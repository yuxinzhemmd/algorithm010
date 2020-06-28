class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def recur(nums,res):
            if len(res) == len(nums):
                ans.append(res[:])
                return
            for i in nums:
                if i in res:
                    continue
                res.append(i)
                recur(nums,res)
                res.pop()
        ans = []
        res = []
        recur(nums,res)
        return ans