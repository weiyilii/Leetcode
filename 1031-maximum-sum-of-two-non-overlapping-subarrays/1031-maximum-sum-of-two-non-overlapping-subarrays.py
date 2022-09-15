class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        l = len(nums)
        first, second = [0]*l, [0]*l
        first[0], second[0] = nums[0], nums[0]
        res = float('-inf')
        
        for i in range(1, firstLen):
            first[i] = first[i-1] + nums[i]
        for i in range(1, secondLen):
            second[i] = second[i-1] + nums[i]
        for i in range(firstLen, l):
            first[i] = first[i-1] + nums[i] - nums[i-firstLen]
        for i in range(secondLen, l):
            second[i] = second[i-1] + nums[i] - nums[i-secondLen]
            
        for i in range(firstLen-1, l):
            for j in range(secondLen-1, l):
                if j - i >= secondLen or i - j >= firstLen:
                    res = max(res, first[i] + second[j])
        return res