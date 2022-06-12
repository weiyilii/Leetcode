class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if words == []:
            return []
        
        n = len(s)
        k = len(words)
        wordlen = len(words[0])
        strlen = wordlen*k
        words_count = collections.Counter(words)
        res = []
        
        def slidingwindow(left):
            # records seen words through iteration
            words_found = collections.defaultdict(int)
            # count how many words in sliding window that matched words_count
            used = 0
            # control if excessive word exists
            excess = False
            # given left, use right starting from left to iterate, increment by wordlen 
            for right in range(left, n, wordlen):
                # determine the operations on word starting from right
                word = s[right: right + wordlen]
                # if word not existing in words_count, reset sliding window 
                # left should move to the right of current right
                # re initiate hashtable, count and boolean
                if word not in words_count:
                    words_found = collections.defaultdict(int)
                    used = 0
                    excess = False
                    left = right + wordlen
                # else: word exists in words_count, we might need it
                else:
                    # check: 1. if current sliding window exceed max length of strlen; 
                    # 2. if there are excessive words in current window
                    # modify sliding window until both are False
                    while right-left >= strlen or excess:
                        # remove one word from left each time
                        remove = s[left: left + wordlen]
                        left += wordlen
                        words_found[remove] -= 1
                        # removed word is exactly the excessive word
                        if words_found[remove] == words_count[remove]:
                            excess = False
                        # the removed word is what we really need
                        else:
                            used -= 1
                    # now word can be added to sliding window        
                    words_found[word] += 1
                    # check if the new added word will be the excessive one
                    if words_found[word] <= words_count[word]:
                        used += 1
                    else:
                        excess = True
                    # if not excessive and exactly used the same number of words
                    # this left index satisfies, append it to answer
                    if used == k and not excess:
                        res.append(left)     
        # only need to iterate from 0 to wordlen - 1: "xbarfoo", "xybarfoo"
        for i in range(wordlen):
            slidingwindow(i)
        
        return res