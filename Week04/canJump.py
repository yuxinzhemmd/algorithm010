class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # k = 0
        # for i in range(len(nums)):
        #     if k == len(nums) -1:
        #         return True
        #     if k < i:    #最大值到达不了下一个点时
        #         return False
        #     k = max(k,nums[i]+i)
        # return True
        # k = 0 
        # for i in range(len(nums)):
        #     if k == len(nums) - 1:
        #         return True
        #     if i > k:
        #         return False
        #     k = max(k,nums[i]+i)
        # return True
        #2.用hashmap优化
        max_reach, n = 0, len(nums)
        for i, x in enumerate(nums):
            if max_reach < i: return False
            if max_reach >= n - 1: return True
            max_reach = max(max_reach, i + x)