class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        count = collections.Counter(sentence)
        return len(count) == 26