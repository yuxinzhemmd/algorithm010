class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        direction = {'up': [0, 1, 'left', 'right'],
                     'down': [0, -1, 'right', 'left'],
                     'left': [-1, 0, 'down', 'up'],
                     'right': [1, 0, 'up', 'down']}
        x, y = 0, 0
        dir = 'up'
        res = 0
        obstacles = set(map(tuple, obstacles))
        for command in commands:
            if command > 0:  # 正数的话进行模型行进操作
                for step in range(command):
                    if (x + direction[dir][0], y + direction[dir][1]) not in obstacles:
                        x += direction[dir][0]
                        y += direction[dir][1]
                        res = max(res, x ** 2 + y ** 2)  #最大欧式距离的平方
                    else:
                        break
            else:  # 负数的话只改变行进方向
                if command == -1:  # 右转
                    dir = direction[dir][3]
                else:  # 即command == -2，左转
                    dir = direction[dir][2]
        return res