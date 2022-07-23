class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        from heapq import heapify, heappush, heappop
        h = [(num[0], i, 0) for i, num in enumerate(nums)]
        heapify(h)
        
        right = max(num[0] for num in nums)
        ans = [float('-inf'), float('inf')] 
        
        while h:
            (left, i, j) = heappop(h)
            if right - left < ans[1] - ans[0]:
                ans = [left, right]
                
            if j == len(nums[i]) - 1:
                return ans
            
            next_elem = nums[i][j+1]
            right = max(right, next_elem)
            heappush(h, (nums[i][j+1], i, j+1))