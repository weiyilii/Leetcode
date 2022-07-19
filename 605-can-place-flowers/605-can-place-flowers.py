class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        l = len(flowerbed)
        for i in range(l):
            if flowerbed[i] == 0:
                left = max(0, i-1)
                right = min(i+1, l-1)
                if flowerbed[left] == 0 and flowerbed[right] == 0:
                    n -= 1
                    flowerbed[i] = 1
        return n <= 0