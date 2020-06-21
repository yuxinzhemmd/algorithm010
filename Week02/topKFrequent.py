class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #1.hash计数，O（nk）
        # hashmap = collections.defaultdict(int)
        # res = []
        # for num in nums:
        #     hashmap[num] += 1


        #2.heap,逐个推
        lookup = Counter(nums)
        res = []
        heap = []
        for num, freq in lookup.items() :
            # 如果堆满了（k个元素）
            if len(heap) == k :
                # 弹出最小频率的元组
                if heap[0][0] < freq:
                    heapq.heapreplace(heap, (freq, num))
            else : 
                heapq.heappush(heap, (freq, num))
        while heap :
            res.append(heapq.heappop(heap)[1])
        
        return res