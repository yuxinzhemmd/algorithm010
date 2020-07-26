class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #hashmap遍历计数
        #row/col/board=row//3*3+col//3
        rows = [collections.defaultdict(int) for i in range(9)]
        columns = [collections.defaultdict(int) for i in range(9)]
        boxes = [collections.defaultdict(int) for i in range(9)]
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_index = (i // 3 ) * 3 + j // 3
                    # keep the current cell value
                    rows[i][num] +=  1
                    columns[j][num] +=  1
                    boxes[box_index][num] +=  1
                    # check if this value has been already seen before
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                        return False
        return True