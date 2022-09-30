class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = -101
        left, right = 0, 0
        while right < len(nums):
            if nums[right] != prev:
                nums[left] = nums[right]
                prev = nums[right]
                left += 1
                right += 1
            else:
                right += 1
        return left