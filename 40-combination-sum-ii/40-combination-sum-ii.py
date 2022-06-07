class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def dfs_sum(target, index, path):
            if target < 0:
                return True
            elif target == 0:
                path.sort()
                return res.append(path)
            else:
                for i in range(index, len(candidates)):
                    if i > index and candidates[i] == candidates[i - 1]:
                        continue
                    if target < candidates[i]:
                        continue
                    dfs_sum(target-candidates[i], i+1, path+[candidates[i]])
        
        res = []
        dfs_sum(target, index = 0, path = [])
        res_set = set(map(tuple, res))
        res = map(list, res_set)
        
        return res