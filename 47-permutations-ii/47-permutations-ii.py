class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        counter = collections.Counter(nums)
        res = []
        
        def dfs(path, counter):
            if len(path) == n:
                res.append(path)
            for num in counter:
                if counter[num] > 0:
                    counter[num] -= 1
                    dfs(path + [num], counter)
                    counter[num] += 1
                    
        dfs([], counter)
        return res