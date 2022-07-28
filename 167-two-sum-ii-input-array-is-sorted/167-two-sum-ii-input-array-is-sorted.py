class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binarySearch(left, right, target):
            while left <= right:
                mid = left + (right - left)//2
                if numbers[mid] == target:
                    return mid
                elif numbers[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        i = 0
        while i < len(numbers) - 1:
            j = binarySearch(i+1, len(numbers)-1, target - numbers[i])
            if j != -1:
                return [i+1, j+1]
            i += 1