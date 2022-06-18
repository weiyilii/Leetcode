class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while n > 1:
            # i2, 3, 5 as 3 pointers track the indexes for multiples of 2, 3, 5
            # once each is min and got appended to ugly number array
            # it will move forward
            u2, u3, u5 = ugly[i2]*2, ugly[i3]*3, ugly[i5]*5
            umin = min(u2, u3, u5)
            ugly.append(umin)
            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            if umin == u5:
                i5 += 1
            n -= 1
        return ugly[-1]