class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 1.两次循环，将非0元素放到0元素上去
        # 2.创建新数组，统计0的个数，放于数组尾部
        # 3.运用一个下标来记录0的位置
        # j = 0
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         nums[j] = nums[i]
        #         if i != j:
        #             nums[i] = 0
        #         j += 1
        # return nums
        # 4.交换0的方法
        zero = 0
        for i in xrange(len(nums)):
            if(nums[i] != 0):
                nums[i],nums[zero] = nums[zero],nums[i]
                zero += 1
        return nums