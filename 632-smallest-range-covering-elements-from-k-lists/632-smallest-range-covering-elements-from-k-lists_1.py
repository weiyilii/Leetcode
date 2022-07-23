class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        # Heap
        # Possible results must be selecting one from each num
        # Maintain a heap that always holds one elem from each num
        # get left by heappop 
        # after pop, push that element's next one (next_elem) to heap
        # right = max(current max, next_elem)
        
        from heapq import heapify, heappush, heappop
        # Initialize heap with all first elements from all num
        h = [(num[0], i, 0) for i, num in enumerate(nums)]
        heapify(h)
        # Initialize right with the max among all first elements (each first is min in their own num)
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
