class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # first is the min
        # second is the second min
        
        first = second = float('inf')
        
        # second gurantees there is one element before is less than second
        # in the process, first might fall behind second
        
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False
