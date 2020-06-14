class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #1.用栈
        rt = 0
        cur = 0
        stack = []
        n = len(height)
        while(cur < n):
            while(stack and height[cur] > height[stack[-1]]):
                h = height[stack[-1]]
                stack.pop()
                if stack == []:
                    break
                minheight = min(height[stack[-1]],height[cur]) #找出当前元素高度与栈顶元素高度的最小值作为最高储水面
                distance = cur - stack[-1] - 1 #当前元素与栈顶元素的距离
                rt = rt + distance * (minheight - h) #算出该层接水量
            stack.append(cur)
            cur += 1
        return rt