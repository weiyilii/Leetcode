class Twitter(object):
    
    from heapq import heappush, heappop

    def __init__(self):
        self.followers = collections.defaultdict(set)
        self.tweets = collections.defaultdict(list)
        self.i = 0

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.tweets[userId].append((self.i, tweetId))
        self.i -= 1

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        h, res = [], []
        users = self.followers[userId]
        users.add(userId)
        for user in users:
            for tweet in self.tweets[user]:
                heappush(h, tweet)
        for j in range(10):
            if not h:
                return res
            res.append(heappop(h)[1])
        return res

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)