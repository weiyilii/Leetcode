class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        m, n = len(houses), len(heaters)
        radius = [0]*m
        houses.sort()
        heaters.sort()
        for i in range(m):
            left, right = 0, n-1
            while left < right:
                mid = left + (right - left)//2
                if heaters[mid] < houses[i]:
                    left = mid + 1
                else:
                    right = mid
            if heaters[left] < houses[i] and left + 1 < n:
                radius[i] = min(abs(heaters[left] - houses[i]),
                             abs(heaters[left + 1] - houses[i]))
            elif heaters[left] > houses[i] and left - 1 >= 0:
                radius[i] = min(abs(heaters[left] - houses[i]),
                             abs(heaters[left - 1] - houses[i]))
            else:
                radius[i] = abs(heaters[left] - houses[i])
        return max(radius)