class Twitter:

    def __init__(self):
        self.followerMap = defaultdict(set)
        self.postMap = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # self.posts.append([userId, tweetId])

        self.postMap[userId].append((self.time, tweetId))
        self.time += 1
        if userId not in self.followerMap:
            self.followerMap[userId]

        

    def getNewsFeed(self, userId: int) -> List[int]:

        posts = list(self.postMap[userId])
        for user in self.followerMap[userId]:
            posts.extend(list(self.postMap[user]))

        posts.sort(key = lambda x : x[0], reverse=True)
        return [p for _, p in posts[:10]]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followerMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followerMap[followerId]:
            self.followerMap[followerId].remove(followeeId)

        
