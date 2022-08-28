class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = "-" if numerator*denominator < 0 else ""
        n, r = divmod(abs(numerator), abs(denominator))
        seen = {}
        res = "."
        
        while r not in seen and r > 0:
            seen[r] = len(res)
            q, r = divmod(r*10, abs(denominator))
            res += str(q)
            
        if r in seen:
            index = seen[r]
            res = res[:seen[r]] + "(" + res[seen[r]:] + ")"
        if res == ".":
            return sign + str(n)
        else:
            return sign + str(n) + res