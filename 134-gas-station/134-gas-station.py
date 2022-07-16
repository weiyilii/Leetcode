class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start, total = 0, 0
        for i in range(len(gas) - 1):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                start = i + 1
        if sum(gas) >= sum(cost):
            return start
        else:
            return -1