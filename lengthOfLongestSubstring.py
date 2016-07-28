# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Given a string, find the length of the longest substring without repeating characters. 
# For example, the longest substring without repeating letters for "abcabcbb" is "abc", 
# which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.


def lengthOfLongestSubstring(s):
    """
    find the length of the longest substring without repeating characters.
    :type s: str
    :rtype: int
    """
    start = 0
    longest = 0
    dicts = {}
    for i in xrange(len(s)):
        if s[i] in dicts and start <= dicts[s[i]]:
            start = dicts[s[i]] + 1
        else:
            longest = max(longest, i - start + 1)
        dicts[s[i]] = i
    return longest


assert lengthOfLongestSubstring('') == 0
assert lengthOfLongestSubstring('dce') == 3
assert lengthOfLongestSubstring('easdfeghjkb') == 10
assert lengthOfLongestSubstring('lalsgflghjk') == 6
assert lengthOfLongestSubstring('abcabdeb') == 5
assert lengthOfLongestSubstring('acbcd') == 3
