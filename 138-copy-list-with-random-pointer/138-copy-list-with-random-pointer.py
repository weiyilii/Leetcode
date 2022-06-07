"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        res = cur = Node(0, head, None)
        # dictionary works as hash, key: old node, value: new node 
        pairs = {}
        
        while head:
            if head not in pairs:
                # if havent seen head in pairs, create new node
                pairs[head] = Node(head.val)
            # no matter the node corresponding to head is newly created
            # or not, we need to let cur point to it
            cur.next = pairs[head]
            # be sure to make cur move forward
            cur = cur.next
            
            # deal with head's random
            if head.random:
                # if the random node head is pointing to not seen,
                # create it
                if head.random not in pairs:
                    pairs[head.random] = Node(head.random.val)
                # set the current new node's random    
                cur.random = pairs[head.random]
            
            head = head.next
            
        return res.next
                
            
            