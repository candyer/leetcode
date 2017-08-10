# leetcode 258 -- Add Digits
# https://leetcode.com/problems/add-digits/description/

# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
# For example:
# Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.


def addDigits1(num):
    """
    :type num: int
    :rtype: int
    """
    if len(str(num)) == 1:
      return num
    res = 0
    for i in range(len(str(num))):
      res += int(str(num)[i])
    return addDigits1(res)


def addDigits2(num):
    """
    :type num: int
    :rtype: int
    """
    if len(str(num)) == 1:
        return num
    return addDigits2(sum([int(i) for i in list(str(num))]))


def addDigits3(num):
    """
    :type num: int
    :rtype: int
    without any loop/recursion in O(1) runtime
    """
    if num == 0:
        return 0
    return (num-1)%9 + 1


def addDigits4(num):
    """
    :type num: int
    :rtype: int
    """
    while num > 9:
        res = 0
        while num:
            res += num%10
            num /=10
        num = res
    return num


print addDigits1(3457) #1
print addDigits1(4568) #5
print addDigits1(3457+4568) #6
print addDigits1(3) #3
print addDigits1(23456789) #8

print addDigits2(3457) #1
print addDigits2(4568) #5
print addDigits2(3457+4568) #6
print addDigits2(3) #3
print addDigits2(23456789) #8

print addDigits3(3457) #1
print addDigits3(4568) #5
print addDigits3(3457+4568) #6
print addDigits3(3) #3
print addDigits3(23456789) #8

print addDigits4(3457) #1
print addDigits4(4568) #5
print addDigits4(3457+4568) #6
print addDigits4(3) #3
print addDigits4(23456789) #8

