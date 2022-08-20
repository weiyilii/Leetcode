class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # DFS
        n = len(nums)
        res = []
        
        def dfs(path, visited):
            if len(path) == n:
                res.append(path)
            for i in range(n):
                if i not in visited:
                    visited.add(i)
                    dfs(path + [nums[i]], visited)
                    visited.remove(i)
        
        dfs([], set())
        return res
