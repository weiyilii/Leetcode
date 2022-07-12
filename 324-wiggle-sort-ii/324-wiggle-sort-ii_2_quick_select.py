class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        copy = list(nums)
        k = len(nums)//2
        median = self.getKthlargest(copy, k)
        copy = self.sort3(copy, median)
        print(copy)
        for i in range(k):
            j = i*2 + 1
            nums[j] = copy[i]
        for i in range(k, len(nums)):
            j = (i-k)*2
            nums[j] = copy[i]
    
    def getKthlargest(self, nums, k):
        
        def quickSelect(left, right):
            p, pivot = left, nums[right]
            for i in range(left, right):
                if nums[i] >= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[right] = nums[right], nums[p]
            if p == k:
                return nums[p]
            elif p < k:
                return quickSelect(p+1, right)
            else:
                return quickSelect(left, p-1)
        
        return quickSelect(0, len(nums)-1)
    
    def sort3(self, nums, median):
      # 3 color sort
        i, j, k = 0, 0, len(nums)-1
        while j <= k:
            if nums[j] > median:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] == median:
                j += 1
            else:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
        return nums
