'''
Leetcode 355 - Design Twitter
Author: Ruowei Chen
Date: 08/Sep/2019
Note:
    1) Left for a while, back to coding tonight.
    2) Follow list can be maintained by a dictionary. Tweets can 
    be a list of tuples of (userId, tweetId).
'''

class Twitter:

    def __init__(self):
        '''
        Initialize data structure here.
        '''
        self.followList = dict() ; 
        # add a pseudo-tweet to avoid empty list.
        self.tweetList = [(-1,-1)] ; 
        return ;
    
    def postTweet(self, userId, tweetId):
        '''
        Compose a new tweet
        '''
        '''
        if tweetId <= self.tweetList[-1][1]:
            tweetId = self.tweetList[-1][1] + 1 ; 
        '''
        self.tweetList.append((userId, tweetId)) ; 
        return ; 

    def getNewsFeed(self, userId):
        '''
        Retrieve the 10 most recent tweet ids in the user's news 
        feed. Each item in the news feed must be posted by users who
        the user followed or by the user herself. Tweets must be 
        ordered from most recent to least recent.
        '''
        userList = [] ; 
        if userId in self.followList:
            userList = self.followList[userId] ; 
        userList.append(userId) ; # include user him/herself.
        result, count = [],0 ; 
        curIndex = len(self.tweetList) - 1 ; 
        while curIndex >= 0 and count < 10:
            if self.tweetList[curIndex][0] in userList:
                result.append(self.tweetList[curIndex][1]) ;
                count += 1 ; 
            curIndex -= 1 ; 
        return result;  

    def follow(self, followerId, followeeId):
        '''
        Follower follows a followee. If the operation is invalid,
        it should be a no-op.
        '''
        if followerId not in self.followList:
            self.followList[followerId] = [followeeId] ; 
        else:
            if followeeId not in self.followList[followerId]:
                self.followList[followerId].append(followeeId) ;
        return ; 

    def unfollow(self, followerId, followeeId):
        '''
        Follower unfollows a followee. If the operation is invalid,
        it should be a no-op.
        '''
        if followerId not in self.followList:
            pass ; 
        else:
            if followeeId not in self.followList[followerId]:
                pass ; 
            else:
                # actually do the work
                self.followList[followerId].remove(followeeId) ;
        return ;


def simpleTest():
    twitter = Twitter() ; 
    twitter.postTweet(1,5) ; 
    print(twitter.getNewsFeed(1)) ; 
    twitter.follow(1,2) ; 
    twitter.postTweet(2,6) ; 
    print(twitter.getNewsFeed(1)) ;
    twitter.unfollow(1,2) ; 
    print(twitter.getNewsFeed(1)) ;
    return ;

def test():
    twitter = Twitter() ; 
    twitter.postTweet(1, 0) ; 
    twitter.postTweet(2, 0) ; 
    twitter.postTweet(1, 3) ;
    twitter.postTweet(2, 2) ; 
    print(twitter.tweetList) ; # debug
    twitter.follow(1,2) ; 
    print(twitter.followList) ; # debug
    twitter.unfollow(2,1) ; 
    twitter.unfollow(1,2) ; 
    print(twitter.followList) ; # debug

    return ;

def main():
    # test() ; 
    simpleTest() ; 
    return ; 

if __name__ == "__main__":
    main() ; 
