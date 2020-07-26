class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def recur(row,col,grid):
            if row >= r or row < 0 or col < 0 or col >= c:
                return
            if grid[row][col] == '0':
                return
            if grid[row][col] == '1':
                grid[row][col] = '0'
                recur(row,col+1,grid)
                recur(row,col-1,grid)
                recur(row-1,col,grid)
                recur(row+1,col,grid)
        if grid == []:
            return 0
        r = len(grid)
        c = len(grid[0])
        res = 0
        for row in range(r):
            for col in range(c):
                if grid[row][col] == '1':
                    res += 1
                    recur(row,col,grid)
        return res