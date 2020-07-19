class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #1.DP
        """
        重复子问题：subproblem[i][j] = min(subproblem[i-1][j],subproblem[i][j-1])

        """
        m = len(grid)
        n = len(grid[0])
        for x in range(1,n):
            grid[0][x] += grid[0][x-1]
        for y in range(1,m):
            grid[y][0] += grid[y-1][0]
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] += min(grid[i-1][j],grid[i][j-1])
        return grid[-1][-1]