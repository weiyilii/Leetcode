class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        m, n = len(key), len(ring)
        pos = dict()
        for i, r in enumerate(ring):
            if r in pos:
                pos[r].append(i)
            else:
                pos[r] = [i]
                    
        state = {0: 0}
        for i in range(m):
            next_state = {}
            for cur_pos in pos[key[i]]:
                next_state[cur_pos] = float('inf')
                for pre_pos in state:
                    next_state[cur_pos] = min(next_state[cur_pos], state[pre_pos] + min(abs(cur_pos - pre_pos), n - abs(cur_pos - pre_pos)))
            state = next_state
        return min(state.values()) + m