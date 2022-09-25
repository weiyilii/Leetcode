class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        i, level = 0, 0
        cur_max, next_max = 0, 0
        while i <= cur_max:
            for j in range(i, cur_max + 1):
                next_max = max(next_max, j + nums[j])
                if next_max >= n-1:
                    return level + 1
            i = cur_max
            cur_max = next_max
            level += 1
        return -1