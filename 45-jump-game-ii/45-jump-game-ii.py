class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l <= 1:
            return 0
        
        i, level = 0, 0
        cur_max, next_max = 0, 0
        
        while i <= cur_max:
            for j in range(i, cur_max + 1):
                next_max = max(next_max, j + nums[j])
                if next_max >= l-1:
                    return level + 1
            i = cur_max + 1
            level += 1
            cur_max = next_max
        return -1