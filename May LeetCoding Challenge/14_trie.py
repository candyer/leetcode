# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3329/


# Implement Trie (Prefix Tree)

# Implement a trie with insert, search, and startsWith methods.

# Example:
# Trie trie = new Trie();

# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");   
# trie.search("app");     // returns true

# Note:
# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.

from collections import defaultdict
class Trie:

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.root = {}
		self.end = '*'
		

	def insert(self, word: str) -> None:
		"""
		Inserts a word into the trie.
		"""
		node = self.root
		for c in word:
			if c not in node:
				node[c] = {}
			node = node[c]
		node[self.end] = True

		

	def search(self, word: str) -> bool:
		"""
		Returns if the word is in the trie.
		"""
		node = self.root
		for c in word:
			if c not in node: 
				return False
			else: 
				node = node[c]
		return self.end in node		


	def startsWith(self, prefix: str) -> bool:
		"""
		Returns if there is any word in the trie that starts with the given prefix.
		"""
		node = self.root
		for c in prefix:
			if c not in node: 
				return False
			else: 
				node = node[c]
		return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)



























