class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # BFS idea, Greedy
        # find possible max reach point in each level
        n = len(nums)
        
        if n <= 1:
            return 0
        
        i, level = 0, 0
        cur_max, next_max = 0, 0
        # i: start of each level
        # cur_max: end of each level, also the possible max reach point in each level
        while i <= cur_max:
            for j in range(i, cur_max+1):
                # find possible max reach point in next level
                next_max = max(next_max, j + nums[j])
                if next_max >= n-1:
                    return level + 1
            level += 1
            cur_max = next_max
            i = j
        return -1
