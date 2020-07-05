class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxnum,end,step = 0,0,0
        for i,num in enumerate(nums[0:-1]):
            if maxnum >= i:
                maxnum = max(maxnum,i+num)
                if i == end:
                    end = maxnum
                    step += 1
        return step