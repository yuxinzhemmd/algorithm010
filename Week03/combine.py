class Solution:
    def combine(self, n, k):
        # def backtrack(first = 1, curr = []):
        #     # if the combination is done
        #     if len(curr) == k:  
        #         output.append(curr[:])
        #     for i in range(first, n + 1):
        #         # add i into the current combination
        #         curr.append(i)
        #         # use next integers to complete the combination
        #         backtrack(i + 1, curr)
        #         # backtrack
        #         curr.pop()
        
        # output = []
        # backtrack()
        # return output
        def recur(i,res):
            if len(res) == k:
                ans.append(res[:])
            for j in range(i,n+1):
                res.append(j)
                recur(j+1,res)
                res.pop()
        qres =[]
        ans =[]
        i = 1
        recur(i,qres)
        return ans