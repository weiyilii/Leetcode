class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # DP, Heap
        # Scan from right to left
        from heapq import heappop, heappush
        n = len(nums)
        dp = [0]*n
        dp[-1] = nums[-1]
        h = [(-dp[-1], n-1)]
        for i in range(n-2, -1, -1):
            val, pos = heappop(h)
            while pos > i+k:
                val, pos = heappop(h)
            heappush(h, (val, pos))
            dp[i] = nums[i] - val
            heappush(h, (-dp[i], i))
        return dp[0]
