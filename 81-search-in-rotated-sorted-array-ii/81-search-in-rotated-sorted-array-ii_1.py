class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        # Only difference with #33 is this allows duplicates,
        # then there will be an edge case that initial nums[left] == nums[right] ([2,5,6,0,0,1,2])
        # Shrink left and right until nums[left] != nums[right]
        # then do the same
        left, right = 0, len(nums) - 1
        while left <= right and nums[left] == nums[right]:
            if nums[left] == target:
                return True
            left += 1
            right -= 1
        
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                return True
            elif nums[mid] >= nums[left]:
                if nums[mid] > target and nums[left] <= target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target and nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
