class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l <= 2:
            return max(nums)
        
        t1, t2 = 0, 0
        for n in nums:
            temp = max(t1 + n, t2)
            t1 = t2
            t2 = temp
        return t2