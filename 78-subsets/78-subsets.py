class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        def dfs(path, prev):
            res.append(path)
            i = prev
            for j in range(i+1, len(nums)):
                dfs(path + [nums[j]], j)
        
        dfs([], -1)
        return res