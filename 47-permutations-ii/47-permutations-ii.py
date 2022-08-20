class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = []
        
        def dfs(path, visited):
            if len(path) == n and path not in res:
                res.append(path)
            for i in range(n):
                if i not in visited:
                    visited.add(i)
                    dfs(path + [nums[i]], visited)
                    visited.remove(i)
                    
        dfs([], set())
        return res