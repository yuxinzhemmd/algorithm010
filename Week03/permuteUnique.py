class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # def recur(nums,res,dic):
        #     if len(res) == len(dic):
        #         ans.append([dic[x] for x in res[:]])
        #         return
        #     for i in dic:
        #         if i in res or :
        #             continue
        #         res.append(i)
        #         recur(nums,res,dic)
        #         res.pop()
        # ans = []
        # res = []
        # dic = {}
        # j = 0
        # for i in nums:
        #     dic[j] = i
        #     j += 1
        # recur(nums,res,dic)
        # new_lst = []
        # for k in ans:
        #     if k not in new_lst:
        #         new_lst.append(k)
        # return new_lst
        nums.sort() # 数组先排序
        self.res = []
        self.recur(nums,[])
        return self.res

    def recur(self,nums,temp):
        if nums == []:
            self.res.append(temp)
            return
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]: #每当进入新的构成，先考虑该构成的首字符是否和上一个一样。
                continue
            self.recur(nums[:i]+nums[i+1:],temp+[nums[i]]) #nums[:i]+nums[i+1:] 避免了重复利用。