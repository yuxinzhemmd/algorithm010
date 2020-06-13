class Solution:
    def twoSum(self, nums, target):
        #1.边判断边插入，O（n）
        hashmap = {}
        for i,num in enumerate(nums):
            another_num = target - num   #所求值 = 目标值-数组值
            if another_num in hashmap:   #是否存在在hashmap里
                return [hashmap[another_num],i] #存在时返回序列
            hashmap[num] = i #将数组加入hashmap
        return []