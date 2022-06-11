class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syms = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        
        res = ''
        for v, s in zip(vals, syms):
            if num == 0:
                break
            value, num = divmod(num, v)
            res += s*value
        return res