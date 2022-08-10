class Solution(object):
    def canMeasureWater(self, jug1Capacity, jug2Capacity, targetCapacity):
        """
        :type jug1Capacity: int
        :type jug2Capacity: int
        :type targetCapacity: int
        :rtype: bool
        """
        x, y, z = jug1Capacity, jug2Capacity, targetCapacity
        if x + y < z:
            return False
        if x == z or y == z or x + y == z:
            return True
        gcd = self.GCD(x, y)
        return z % gcd == 0        
    
    def GCD(self, a, b):
        while b != 0:
            a, b = b, a%b
        return a