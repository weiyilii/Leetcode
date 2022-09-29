class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def getHours(k):
            hour = 0
            for p in piles:
                hour += p//k
                if p%k > 0:
                    hour += 1
            return hour
        
        def leftBound(target):
            left, right = 1, max(piles)
            while left <= right:
                mid = left + (right - left)//2
                if getHours(mid) < target:
                    right = mid - 1
                elif getHours(mid) == target:
                    right = mid - 1
                elif getHours(mid) > target:
                    left = mid + 1
            return left
        
        return leftBound(h)