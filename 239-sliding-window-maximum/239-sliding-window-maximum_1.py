class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Max queue
        # queue stores indexes of num not number itself
        q = collections.deque()
        res = []
        for i in range(len(nums)):
            # remove elements from left that is lefter than sliding window
            # worst case is only lefter by 1 so no need to use while
            if q and q[0] < i-k+1:
                q.popleft()
            # remain leftest element is the largest
            # everytime an element is coming into the queue
            # pop element which is less it from the tail
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            # only when i has iterated >= k elements, start appending results
            if i + 1 >= k:
                res.append(nums[q[0]])
        return res
