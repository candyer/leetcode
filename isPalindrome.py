# Leetcode 9 -- Palindrome Number

# Determine whether an integer is a palindrome. Do this without extra space.

def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0: return False
    div = 1
    while x/div >= 10:
        div = div * 10
    while x:       
        if x / div != x % 10:
            return False
        x = ( x % div ) / 10
        div = div / 100
    return True


assert isPalindrome(-1) == False
assert isPalindrome(0) == True
assert isPalindrome(3) == True
assert isPalindrome(123) == False
assert isPalindrome(123321) == True
assert isPalindrome(2332) == True
assert isPalindrome(33) == True
assert isPalindrome(12301321) == False
