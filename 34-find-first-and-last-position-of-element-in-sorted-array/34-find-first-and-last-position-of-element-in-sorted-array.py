class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def left_bound(target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left)//2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] == target:
                    right = mid - 1
                elif nums[mid] > target:
                    right = mid - 1
            if left == len(nums):
                return -1
            return left if nums[left] == target else -1
        
        def right_bound(target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left)//2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] == target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
            if right < 0:
                return -1
            return right if nums[right] == target else -1
        
        return [left_bound(target), right_bound(target)]