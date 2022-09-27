class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(path, used):
            if len(path) == len(nums):
                res.append(path)
                return
            for n in nums:
                if n not in used:
                    used.add(n)
                    backtrack(path + [n], used)
                    used.remove(n)
                    
        backtrack([], set())
        return res