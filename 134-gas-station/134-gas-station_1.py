class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # 2 conditions:
        # 1. total gas >= total cost (if so, there must be an answer)
        # 2. if starts at A, cannot reach B, starting from any station between A and B cannot reach B (B is the first station A cannot reach)
        
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
