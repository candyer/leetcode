class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        dicts = {}
        res = set()
        nums.sort()
        for a in xrange(len(nums)):
            for b in xrange(a+1,len(nums)):
                if not nums[a] + nums[b] in dicts:
                    dicts[nums[a] + nums[b]] = [(a,b)]
                else:
                    dicts[nums[a] + nums[b]].append((a,b))
    
        for c in xrange(len(nums)):
            for d in xrange(c+1, len(nums)):
                t = target - nums[c] - nums[d]
                if t in dicts:
                    for pair in dicts[t]:
                        if pair[0] > d: 
                            res.add((nums[c],nums[d],nums[pair[0]],nums[pair[1]]))
        ans = []
        for i in res:
            ans.append(list(i))
        return ans
