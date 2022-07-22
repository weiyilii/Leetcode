class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Greedy
        # Check balance of unclosed "("
        # if current is "(": open balance += 1
        # elif current is ")": it can close previous closet "(", open balance -= 1
        # else: current is "*": it can serve as "(" or ")":
        #       if serve as ")", open balance -= 1; 
        #       if serve as "*", open balance no change
        #       if serve as "(", open balance += 1
        # use min and max open to record both possibilities
        
        min_open, max_open = 0, 0
        for c in s:
            if c == '(':
                min_open += 1
                max_open += 1
            elif c == ')':
                min_open -= 1
                max_open -= 1
            else:
                min_open -= 1
                max_open += 1
                
            # through the whole process max_open must be >= 0: otherwise that means too many ")", even regard "*" as "(", ")" still too many
            if max_open < 0:
                return False
            
            elif min_open < 0: # too many *
                min_open = 0
        
        return min_open == 0
