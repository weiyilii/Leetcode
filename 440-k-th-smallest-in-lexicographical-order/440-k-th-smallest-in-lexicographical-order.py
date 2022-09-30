class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        k -= 1
        res = 1
        while k > 0:
            interval = [res, res+1]
            count = 0
            while interval[0] <= n:
                count += min(n+1, interval[1]) - interval[0]
                interval = [interval[0]*10, interval[1]*10]
            if count > k:
                k -= 1
                res *= 10
            else:
                k -= count
                res += 1
        return res