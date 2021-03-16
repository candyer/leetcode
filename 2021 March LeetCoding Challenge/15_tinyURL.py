# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/590/week-3-march-15th-march-21st/3673/

# Encode and Decode TinyURL


# Note: This is a companion problem to the System Design problem: Design TinyURL.
# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl 
# and it returns a short URL such as http://tinyurl.com/4e9iAk.

# Design the encode and decode methods for the TinyURL service. 
# There is no restriction on how your encode/decode algorithm should work. 
# You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.


from string import ascii_letters, digits
from random import randint

class Codec:

    def __init__(self):
        self.string = ascii_letters + digits
        self.full_to_tiny = {}
        self.tiny_to_full = {}
        self.url_head = 'http://tinyurl.com/'

    def shorten_url(self):
        """randomly select 6 characters from self.string"""
        return ''.join([self.string[randint(1, 61)] for _ in range(6)])
            
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        if longUrl in self.full_to_tiny:
            return self.url_head + self.full_to_tiny[longUrl]
        else:
            tail = self.shorten_url(longUrl)
            self.full_to_tiny[longUrl] = tail
            self.tiny_to_full[tail] = longUrl
            return  self.url_head + tail

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        tail = shortUrl[-6:]
        if tail in self.tiny_to_full:
            return self.tiny_to_full[tail]
        else:
            return None
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))


