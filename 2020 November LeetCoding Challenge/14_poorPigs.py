# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/565/week-2-november-8th-november-14th/3530/
# https://potatomatooo.blogspot.com/2020/11/leetcode-458-poor-pigs-python.html

# Poor Pigs

# There are 1000 buckets, one and only one of them is poisonous, while the rest are filled with water. 
# They all look identical. If a pig drinks the poison it will die within 15 minutes. 
# What is the minimum amount of pigs you need to figure out which bucket is poisonous within one hour?

# Answer this question, and write an algorithm for the general case.


# General case:
# If there are n buckets and a pig drinking poison will die within m minutes, 
# how many pigs (x) you need to figure out the poisonous bucket within p minutes? There is exactly one bucket with poison.


# Note:
# A pig can be allowed to drink simultaneously on as many buckets as one would like, and the feeding takes no time.
# After a pig has instantly finished drinking buckets, there has to be a cool down time of m minutes. During this time, 
# only observation is allowed and no feedings at all.
# Any given bucket can be sampled an infinite number of times (by an unlimited number of pigs).


from math import ceil, log
def poorPigs(buckets: int, minutesToDie: int, minutesToTest: int) -> int:
	max_buckets_for_one_pig = minutesToTest // minutesToDie + 1
	return ceil(log(buckets, max_buckets_for_one_pig))

assert(poorPigs(1000, 15, 60) == 5)


