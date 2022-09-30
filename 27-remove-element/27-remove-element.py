class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] != val:
                left += 1
            else:
                while right >= 0 and nums[right] == val:
                    right -= 1
                if right > left:
                    nums[left] = nums[right]
                    left += 1
                    right -= 1
        return left
        