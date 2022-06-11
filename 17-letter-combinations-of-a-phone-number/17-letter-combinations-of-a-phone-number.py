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
        
        res = []
        # recursion
        def dfs(index, path, res):
            if index > len(digits) - 1:
                res.append(path)
                return
            else:
                for i in dic[digits[index]]:
                    dfs(index+1, path+i, res)
        
        dfs(0, '', res)
        
        return res