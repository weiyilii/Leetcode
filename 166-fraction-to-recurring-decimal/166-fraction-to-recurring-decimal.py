class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = '-' if numerator*denominator < 0 else ''
        i, remainder = divmod(abs(numerator), abs(denominator))
        r = {}
        res = '.'
        # r tracks all remainders, if new remainder has been in r, remainder will repeat
        while remainder > 0 and remainder not in r:
            # len(res) will tell where to insert "("
            r[remainder] = len(res)
            n, remainder = divmod(remainder*10, abs(denominator))
            res += str(n)
        if remainder in r:
            index = r[remainder]
            res = res[:index] + '(' + res[index:] + ')'
        return str(sign) + str(i) + res if res != '.' else str(sign) + str(i)