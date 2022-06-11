class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        dic = {
            '2': 'a b c'.split(),
            '3': 'd e f'.split(),
            '4': 'g h i'.split(),
            '5': 'j k l'.split(),
            '6': 'm n o'.split(),
            '7': 'p q r s'.split(),
            '8': 't u v'.split(),
            '9': 'w x y z'.split()
        }
        
        res = [""]
        for i in digits:
            res = [item+letter for item in res for letter in dic[i]]
        
        return res
