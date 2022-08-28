class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = collections.Counter(nums)
        numbers = sorted(count.keys(), reverse = True)
        l = len(numbers)
        take, ntake = [0]*l, [0]*l
        take[0] = numbers[0]*count[numbers[0]]
        for i in range(1, l):
            if numbers[i] == numbers[i-1] - 1:
                take[i] += ntake[i-1] + numbers[i]*count[numbers[i]]
            else:
                take[i] += max(take[i-1], ntake[i-1]) + numbers[i]*count[numbers[i]]
            ntake[i] += max(take[i-1], ntake[i-1])
        
        return max(take[-1], ntake[-1])