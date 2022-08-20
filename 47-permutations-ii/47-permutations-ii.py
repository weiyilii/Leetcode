class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # DFS, Backtracking
        n = len(nums)
        counter = collections.Counter(nums)
        res = []
        
        def dfs(path, counter):
            if len(path) == n:
                res.append(path)
            # each step, instead of iterating over all candidates, just visit all unique numbers
            for num in counter:
                if counter[num] > 0:
                    counter[num] -= 1
                    dfs(path + [num], counter)
                    counter[num] += 1
                    
        dfs([], counter)
        return res
