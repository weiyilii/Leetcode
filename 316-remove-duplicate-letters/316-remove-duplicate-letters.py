class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # determine last index of each letter's occurence
        last_index = {} 
        # track elements in stack
        seen = set()
        # for giving distinct letters in smallest lexicographical order
        stack = []
        n = len(s)
        
        for i in range(n):
            last_index[s[i]] = i
            
        for i in range(n):
            if s[i] not in seen:
                # when letters in stack is larger than current s[i] and those letters 
                # are not unique and will occur in string later
                # pop them out and update seen
                while stack and s[i] < stack[-1] and last_index[stack[-1]] > i-1:
                    seen.remove(stack.pop())
                stack.append(s[i])
                seen.add(s[i])
        return ''.join(stack)