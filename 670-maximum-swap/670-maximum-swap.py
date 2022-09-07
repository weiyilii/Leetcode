class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = [n for n in str(num)]
        l = len(digits)
        max_idx = l - 1
        x, y = 0, 0
        
        for i in range(l-1, -1, -1):
            if digits[i] > digits[max_idx]:
                max_idx = i
            elif digits[i] < digits[max_idx]:
                x, y = i, max_idx
        digits[x], digits[y] = digits[y], digits[x]
        return int("".join(digits))