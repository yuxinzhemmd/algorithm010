class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #1.python方便解法
        # n = len(nums)
        # k %= n
        # for _ in range(k):
        #     nums.insert(0, nums.pop())
        #2.python方便解法
        # n = len(nums)
        # k %= n
        # nums[:] = nums[-k:] + nums[:-k]
        #3分开倒转
        n = len(nums)
        k %= n
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]