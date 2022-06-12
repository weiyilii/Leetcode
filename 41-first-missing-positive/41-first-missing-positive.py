class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # for a nums with a length of l, possible result can only be 1, 2, ...l+1
        # append 0, index will range from 1 to l+1 (n)
        # use index as hash
        nums.append(0)
        n = len(nums)
        for i in range(n):
            # if element is not positive or >= n, it will not be answer, set it to 0
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        # now all elements range from 0 to n-1
        # scale each element by n to record the frequency of index appearing as number
        for i in range(n):
            nums[nums[i] % n] = nums[nums[i] % n] + n
        # check elements nums[1] to nums[n-1]
        # if any nums[index] is between 0 and n-1 (has not been modified)
        # that means index has not appeared among the elements in nums
        # return that index
        for i in range(1, n):
            if nums[i]/n == 0:
                return i
        # the answer is n
        return n
                
            