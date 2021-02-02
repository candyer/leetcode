# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3598/


# Word Ladder


# Given two words beginWord and endWord, and a dictionary wordList, 
# return the length of the shortest transformation sequence from beginWord to endWord, such that:

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list.
# Return 0 if there is no such transformation sequence.


# Example 1:
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog", return its length 5.

# Example 2:
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
 

# Constraints:
# 1 <= beginWord.length <= 100
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the strings in wordList are unique.

from typing import List
from collections import defaultdict, deque
def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    n = len(beginWord)
    words_tranform = defaultdict(list)
    for word in wordList:
        for i in range(n):
            tmp = word[:i] + '*' + word[i + 1:]
            words_tranform[tmp].append(word)

    queue = deque([[beginWord, 1]])
    visited = {beginWord: True}
    while queue:
        cur_word, count = queue.popleft()
        for i in range(n):
            nxt_word = cur_word[:i] + '*' + cur_word[i + 1:]
            for word in words_tranform[nxt_word]:
                if word == endWord:
                    return count + 1
                if word not in visited:
                    visited[word] = True
                    queue.append([word, count + 1])
            words_tranform[nxt_word] = []
    return 0   

assert(ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == 5)
assert(ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]) == 0)
assert(ladderLength("hit", "hot", ["hot"]) == 2)
       



