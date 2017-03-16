# Leetcode 66 -- Plus One 

# Given a non-negative number represented as an array of digits, plus one to the number.
# The digits are stored such that the most significant digit is at the head of the list.

# solution 1,  the stupid solution
def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    n = len(digits)
    num = 0
    for i in xrange(n):
        num += digits[i]* (10**(n-i-1))
    return [int(i) for i in str(num+1)]

# solution 2
def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    for i in xrange(len(digits)-1,-1,-1):
        if digits[i] != 9:
            digits[i] += 1
            return digits[:i] + [digits[i]] + [0]*(len(digits)-i-1)
    return [1] + [0]*len(digits)

# solution 3  this solution works for adding any integers.
def plusOne(digits, carry=1):
    """
    :type digits: List[int]
    :rtype: List[int]
    """    
    res = []
    for digit in reversed(digits):
        val = digit + carry
        carry = val / 10
        res.append(val % 10)
    while carry:
        res.append(carry % 10)
        carry /= 10
    return list(reversed(res))


print plusOne([]) #[1]
print plusOne([0]) #[1] 
print plusOne([2,5,7]) #[2,5,8]
print plusOne([9,9,9,9]) #[1,0,0,0,0]
print plusOne([9,9,1,9,9]) #[9,9,2,0,0]
print plusOne([1,9,9,9]) #[2,0,0,0]
