class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Binary Search
        
        nums.sort()
        n = len(nums)
        res = set()
        
        for i in range(n-1):
            target = nums[i] + k
            left, right = i+1, n-1
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            if nums[left] == target:
                res.add((nums[i], nums[left]))
        return len(res)
