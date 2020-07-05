class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five = 0
        ten = 0
        for i in bills:
            if i == 5:
                five += 1
            if i == 10:
                ten += 1
                if five:
                    five -= 1
                else:
                    return False
            if i == 20:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True