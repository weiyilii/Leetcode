class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = [n for n in str(num)]
        max_idx = len(digits) - 1
        x, y = 0, 0
        
        for i in range(len(digits))[::-1]:
            if digits[i] > digits[max_idx]:
                max_idx = i
            elif digits[i] < digits[max_idx]:
                x = i
                y = max_idx
        
        digits[x], digits[y] = digits[y], digits[x]
        
        return int(''.join(digits))