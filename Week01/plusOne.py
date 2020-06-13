class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = [0] + digits
        i = len(digits) -1
        digits[i] += 1
        while(i > 0 ):
            if(digits[i] == 10):
                digits[i] = 0
                digits[i - 1] += 1
            i -= 1
        if digits[0] == 0:
            digits.remove(0)
        return digits