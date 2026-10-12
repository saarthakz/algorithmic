"""
Implement a simplified version of Twitter which allows users to post tweets, follow/unfollow each other, and view the 10 most recent tweets within their own news feed.

Users and tweets are uniquely identified by their IDs (integers).

Implement the following methods:

    * Twitter() Initializes the twitter object.

    * void postTweet(int userId, int tweetId) Publish a new tweet with ID tweetId by the user userId. You may assume that each tweetId is unique.

    * List<Integer> getNewsFeed(int userId) Fetches at most the 10 most recent tweet IDs in the user's news feed. Each item must be posted by users who the user is following or by the user themself. Tweets IDs should be ordered from most recent to least recent.

    * void follow(int followerId, int followingId) The user with ID followerId follows the user with ID followingId.

    * void unfollow(int followerId, int followingId) The user with ID followerId unfollows the user with ID followingId.

"""

from typing import Dict, Set, List, Tuple
import heapq


class Twitter:

    def __init__(self):
        # UserID -> Set of all the people they follow
        self.follower_following_mp: Dict[int, Set[int]] = {}

        # UserID -> Set of people who follow them
        self.following_follower_mp: Dict[int, Set[int]] = {}

        # UserID -> List of (Timestamp, TweetID), oldest to newest
        self.user_tweet_map: Dict[int, List[Tuple[int, int]]] = {}

        self.timestamp = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweet_map.setdefault(userId, []).append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        user_following = self.follower_following_mp.get(userId, set()).copy()

        # Include the user themself
        user_following.add(userId)

        # Heap entries: (-timestamp, tweetId, userId, tweetIndex)
        max_heap = []

        # Add only the newest tweet from each user
        for user in user_following:
            tweets = self.user_tweet_map.get(user, [])

            if tweets:
                idx = len(tweets) - 1
                timestamp, tweetId = tweets[idx]

                heapq.heappush(max_heap, (-timestamp, tweetId, user, idx))

        recent_ten = []

        while max_heap and len(recent_ten) < 10:
            _, tweetId, user, idx = heapq.heappop(max_heap)
            recent_ten.append(tweetId)

            # Add the next older tweet from this same user
            idx -= 1

            if idx >= 0:
                timestamp, next_tweetId = self.user_tweet_map[user][idx]

                heapq.heappush(max_heap, (-timestamp, next_tweetId, user, idx))

        return recent_ten

    def follow(self, followerId: int, followingId: int) -> None:
        if followerId == followingId:
            return

        self.follower_following_mp.setdefault(followerId, set()).add(followingId)

        self.following_follower_mp.setdefault(followingId, set()).add(followerId)

    def unfollow(self, followerId: int, followingId: int) -> None:
        if followerId == followingId:
            return

        self.follower_following_mp.get(followerId, set()).discard(followingId)

        self.following_follower_mp.get(followingId, set()).discard(followerId)
