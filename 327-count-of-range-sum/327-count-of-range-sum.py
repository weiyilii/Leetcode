class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        first = [0]
        for num in nums:
            first.append(first[-1] + num)
        
        def helper(low, high):
            mid = low + (high - low) // 2
            if mid == low:
                return 0
            
            count = helper(low, mid) + helper(mid, high)
            
            i = j = mid
            for start in first[low:mid]:
                while i < high and first[i] - start < lower:
                    i += 1
                while j < high and first[j] - start <= upper:
                    j += 1
                count += j - i
            first[low:high] = sorted(first[low:high])
            return count
        
        return helper(0, len(first))
        