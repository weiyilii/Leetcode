class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        # Scan twice: from left to right, from right to left
        # left2right gurantees right neighbor has more candies if right rating is higher
        # right2left gurantees left neighbor has more candies if left rating is higher
        # res will take max of each element
        
        n = len(ratings)
        left2right = [1 for _ in range(n)]
        right2left = [1 for _ in range(n)]
        res = []
        
        for i in range(n-1):
            if ratings[i] < ratings[i+1]:
                left2right[i+1] = left2right[i] + 1
        
        for i in range(1, n)[::-1]:
            if ratings[i-1] > ratings[i]:
                right2left[i-1] = right2left[i] + 1
        
        for i in range(n):
            res.append(max(left2right[i], right2left[i]))
        
        return sum(res)
