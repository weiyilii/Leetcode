class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.mergeSort(nums, 0, len(nums)-1)
        return nums
    
    def mergeSort(self, nums, leftStart, rightEnd):
        if leftStart >= rightEnd:
            return
        else:
            mid = (leftStart + rightEnd) // 2
            self.mergeSort(nums, leftStart, mid)
            self.mergeSort(nums, mid+1, rightEnd)
            self.mergeHalves(nums, leftStart, rightEnd)
    
    def mergeHalves(self, nums, leftStart, rightEnd):
        mid = (leftStart + rightEnd) // 2
        temp = []
        left = leftStart
        right = mid + 1
        while left <= mid and right <= rightEnd:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1
        temp += (nums[left:mid+1] + nums[right:rightEnd+1])
        nums[leftStart:rightEnd+1] = temp
