def removeDuplicates80(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #solution 1, O(n) memory, not good!
    d = {}
    for num in nums:
        d[num] = d.get(num,0) + 1 
    
    count = 0
    for num in set(nums):
        if d[num] > 1:
            count = count + 2
        else:
            count = count + 1
    return count

    #solution 2
    if len(nums) < 3: return len(nums)

    count = 1
    for i in range(2, len(nums)):
        if nums[i] != nums[count] or nums[i] != nums[count - 1]:
            count += 1
            nums[count] = nums[i]
    return count + 1

print removeDuplicates80([1,1,1,2,2,3]) #5
print removeDuplicates80([1,1,1,2,2,2,3,3,3]) #6
