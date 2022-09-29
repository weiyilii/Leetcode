class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def getDay(cap):
            s, day = 0, 1
            for w in weights:
                if s + w <= cap:
                    s += w
                else:
                    s = w
                    day += 1
            return day
        
        def leftBound(target):
            left, right = max(weights), sum(weights)
            while left <= right:
                mid = left + (right - left)//2
                if getDay(mid) < target:
                    right = mid - 1
                elif getDay(mid) == target:
                    right = mid - 1
                elif getDay(mid) > target:
                    left = mid + 1
            return left
        
        return leftBound(days)