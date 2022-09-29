class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        
        def helper(arr):
            t1, t2 = 0, 0
            for n in arr:
                temp = max(t1 + n, t2)
                t1 = t2
                t2 = temp
            return t2
        
        return max(helper(nums[1:]), helper(nums[:-1]))