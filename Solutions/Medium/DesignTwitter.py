from collections import heapq
from collections import defaultdict
from collections import List

class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.count = 0
        self.tweetMap = defaultdict(list)



    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        newsFeed = []
        minHeap = []
        self.followMap[userId].add(userId)
        for fid in self.followMap[userId]:
            if fid in self.tweetMap:
                index = len(self.tweetMap[fid]) - 1
                count, tid = self.tweetMap[fid][index]
                minHeap.append([count, tid, fid, index - 1])
        
        heapq.heapify(minHeap)
        while minHeap and len(newsFeed) < 10:
            count, tid, fid, index = heapq.heappop(minHeap)
            newsFeed.append(tid)
            if index >= 0:
                count, tid = self.tweetMap[fid][index]
                heapq.heappush(minHeap, [count, tid, fid, index - 1])

        return newsFeed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
