class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        def dfs(path, visited):
            res.append(path)
            i = visited[-1]
            for j in range(i+1, len(nums)):
                visited.append(j)
                dfs(path + [nums[j]], visited)
                visited.pop()
        
        dfs([], [-1])
        return res