class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        
        def dfs(path, prev):
            res.append(path)
            unique = {}
            for i in range(prev+1, len(nums)):
                if nums[i] not in unique:
                    unique[nums[i]] = i
            for key in unique:
                dfs(path + [key], unique[key])
        
        dfs([], -1)
        return res