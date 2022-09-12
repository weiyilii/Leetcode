class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        if len(cards) == 1:
            return abs(cards[0] - 24.0) <= 0.1
                
        for i in range(len(cards) - 1):
            for j in range(i+1, len(cards)):
                num1, num2 = cards[i], cards[j]
                new = [number for k, number in enumerate(cards) if (k != i and k != j)]
                nums = [num1 + num2, num1 - num2, num2 - num1, num1*num2]
                if num1 != 0:
                    nums.append(float(num2)/num1)
                if num2 != 0:
                    nums.append(float(num1)/num2)
                for n in nums:
                    new.append(n)
                    if self.judgePoint24(new):
                        return True
                    new.pop()
        return False