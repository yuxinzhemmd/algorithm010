class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #1.排序分类，O（NKLogK）
        # ans = collections.defaultdict(list)
        # for s in strs:
        #     ans[tuple(sorted(s))].append(s)
        # return ans.values()
        #2.计数分类，
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for i in s:
                count[ord(i) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()