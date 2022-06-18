class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        n = len(secret)
        bulls, cows = 0, 0
        s, g = collections.defaultdict(int), collections.defaultdict(int)
        for i in range(n):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                s[secret[i]] += 1
                g[guess[i]] += 1
        for key in s:
            cows += min(s[key], g[key])
        return str(bulls) + 'A' + str(cows) + 'B'