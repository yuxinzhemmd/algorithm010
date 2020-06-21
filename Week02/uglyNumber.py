# class Solution(object):
#     def nthUglyNumber(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#       1.heap,预先生成1690个丑数，根据n到heap中取
class Ugly(object):
    def __init__(self):
        hp = [1]
        self.res = res = []
        set1 = set()
        heapq.heapify(hp)
        for i in range(1690):
            a = heapq.heappop(hp)
            for j in [2,3,5]:
                n = a*j
                if n not in set1:
                    heapq.heappush(hp,n)
                    set1.add(n)
            res.append(a)
class Solution(object):
    u = Ugly()
    def nthUglyNumber(self, n):
        return self.u.res[n-1]