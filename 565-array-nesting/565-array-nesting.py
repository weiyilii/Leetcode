class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def dfs(i):
            if nums[i] not in s:
                s.add(nums[i])
                visited.add(nums[i])
                dfs(nums[i])
        
        res = 0
        visited = set()
        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                s = set()
                dfs(i)
                res = max(res, len(s))
        return res