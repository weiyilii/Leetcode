class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n-1
        lmax, rmax = 0, 0
        res = 0
        
        while left < right:
            lmax = max(lmax, height[left])
            rmax = max(rmax, height[right])
            
            if lmax <= rmax:
                res += lmax - height[left]
                left += 1
            else:
                res += rmax - height[right]
                right -= 1
        return res