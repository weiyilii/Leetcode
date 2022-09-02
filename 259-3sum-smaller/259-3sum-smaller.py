class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = len(nums)
        if l < 3:
            return 0
        
        nums.sort()
        res = 0
        p1, p2, p3 = 0, 1, 2
        for p1 in range(l-2):
            if nums[p1] > 0 and nums[p1] > target:
                break
            sum2 = target - nums[p1]
            for p2 in range(p1+1, l-1):
                if nums[p2] > 0 and nums[p2] > sum2:
                    break
                for p3 in range(p2+1, l):
                    if nums[p3] < sum2 - nums[p2]:
                        res += 1
                        #print(p1, p2, p3)
                    else:
                        break
        return res