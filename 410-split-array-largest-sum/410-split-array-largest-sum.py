class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        def getM(cap):
            m, subsum = 1, 0
            for n in nums:
                if n + subsum <= cap:
                    subsum += n
                else:
                    subsum = n
                    m += 1
            return m
        
        left, right = max(nums), sum(nums)
        while left <= right:
            mid = left + (right - left)//2
            if getM(mid) < m:
                right = mid - 1
            elif getM(mid) == m:
                right = mid - 1
            elif getM(mid) > m:
                left = mid + 1
        return left